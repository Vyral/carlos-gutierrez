import os
filedir = "_posts/"
dirs = os.listdir(filedir)


for postfile in dirs:
	post = '_posts/' + postfile

	def addFrontMatter():
		post = '_posts/' + postfile
		file = open(post, 'r+', encoding='utf-8', errors='ignore')
		yt = file.read()
		ytcode = yt.partition('https://img.youtube.com/vi/')[2].partition('"')[0]
		ytcode = ytcode[:11]
		newline = yt.replace('---', '---\nyoutube_code: '+ ytcode + '\nexcerpt:\nenclosure:\npullquote:\nenclosure_type: video/mp4\nenclosure_time:\nuse_youtube_image: true\nyoutube_alternate_image: /img/cover.jpg', 1)
		file = open(post, 'w')
		file.seek(0)
		file.write(newline)
		file.close()

	def cleanPost():
		post = '_posts/' + postfile
		file = open(post, 'r+', encoding='utf-8', errors='ignore')
		yt = file.read()
		frontmatter = yt.rpartition('---')[0]
		post = yt.partition('</iframe>')[2]
		ytpost = "---\n{% include youtube.html %}\n" + post
		fullpost = (frontmatter + ytpost)
		file.seek(0)
		file.write(fullpost)
		file.close()

	def removePost():
		if post.endswith('.html'):
			os.remove(post)

	removePost()
	if post.endswith('.md') and post != '_posts/_defaults.md':
		addFrontMatter()
		cleanPost()
		print('Post Setup Complete for ' + post)
