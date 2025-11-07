from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# ホームページ
def index(request):
    '''学習ノートのホームページ'''
    return render(request, "learning_logs/index.html")


# トピック一覧
@login_required
def topics(request):
    '''すべてのトピックを表示する'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, "learning_logs/topics.html", context)


# 個別トピックのページ
@login_required
def topic(request, topic_id):
    '''トピックの全ての記事を表示'''
    topic = Topic.objects.get(id=topic_id)

    # トピックが現在のユーザーが所持するものであることを確認する
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, "learning_logs/topic.html", context)


# 新規トピック追加ページ（フォーム）
@login_required
def new_topic(request):
    # 新規トピックの追加
    if request.method != 'POST':
        # データ送信されていない場合、空のフォームを生成
        form = TopicForm()
    else:
        # データ送信された場合
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # 空のフォームを表示
    context = {'form': form}
    return render(request, "learning_logs/new_topic.html", context)


# 新規記事追加ページ（フォーム）
@login_required
def new_entry(request, topic_id):
    '''特定のトピックに新規記事を追加する'''
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # データ送信されていない場合、空のフォームを生成
        form = EntryForm()
    else:
        # データ送信された場合
        form = EntryForm(data=request.POST)  # EntryFormクラスをインスタンス化
        if form.is_valid():
            new_entry = form.save(commit=False)  # Entryクラス（モデル）をインスタンス化
            new_entry.topic = topic  # 生成したEntryのインスタンスにtopicを代入。
            new_entry.save()  # DBに保存（テーブルにインサート）
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


# 記事の編集ページ
@login_required
def edit_entry(request, entry_id):
    '''既存の記事を編集する'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # トピックが現在のユーザーが所持するものであることを確認する
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初回リクエスト時は現在の記事の内容がフォームに埋め込まれている
        form = EntryForm(instance=entry)
    else:
        # POSTでデータが送信されたとき（編集時）
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
