import praw
import json
import tkinter as tk
from tkinter import messagebox


# Inicialização da API do Reddit (substitua com suas credenciais)
reddit = praw.Reddit(client_id='SEU_CLIENT_ID', 
                     client_secret='SEU_CLIENT_SECRET', 
                     user_agent='SEU_USER_AGENT')



# Função para extrair todos os comentários e respostas
def extract_comments(post_id):
    submission = reddit.submission(id=post_id)
    submission.comments.replace_more(limit=None)
    comments_data = []
    total_comments = 0
    total_replies = 0

    for comment in submission.comments.list():
        total_comments += 1
        comment_data, num_replies = process_comment(comment)
        comments_data.append(comment_data)
        total_replies += num_replies

    return comments_data, total_comments, total_replies

# Função para processar um único comentário e suas respostas
def process_comment(comment):
    num_replies = 0
    replies_data = []
    for reply in comment.replies:
        if isinstance(reply, praw.models.MoreComments):
            continue
        reply_data, num_nested_replies = process_comment(reply)
        replies_data.append(reply_data)
        num_replies += 1 + num_nested_replies

    comment_data = {
        "id": comment.id,
        "author": comment.author.name if comment.author else "Deleted",
        "body": comment.body,
        "replies": replies_data
    }

    return comment_data, num_replies

# Função para iniciar a raspagem de comentários
def start_scraping():
    post_id = entry_post_id.get()
    if not post_id:
        messagebox.showinfo("Erro", "Por favor, insira o ID do post.")
        return
    try:
        global comments
        comments, total_comments, total_replies = extract_comments(post_id)
        messagebox.showinfo("Concluído", f"Scraping concluído!\nTotal de comentários: {total_comments}\nTotal de respostas: {total_replies}")
        button_save.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para salvar os comentários em um arquivo JSON
def save_comments():
    with open('reddit_comments.json', 'w') as file:
        json.dump(comments, file)
    messagebox.showinfo("Salvo", "Arquivo salvo como 'reddit_comments.json'")

# Configuração da janela da interface gráfica
root = tk.Tk()
root.title("Reddit Scraper")

# Criação dos widgets
label = tk.Label(root, text="ID do Post:")
entry_post_id = tk.Entry(root)
button_scrape = tk.Button(root, text="Scrape", command=start_scraping)
button_save = tk.Button(root, text="Save", command=save_comments, state=tk.DISABLED)

# Organização dos widgets
label.pack(pady=5)
entry_post_id.pack(pady=5)
button_scrape.pack(pady=5)
button_save.pack(pady=5)

# Iniciar a interface gráfica
root.mainloop()
