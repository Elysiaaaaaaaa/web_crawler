import aiohttp
import asyncio

async def fetch_page(session, url, path):
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.text()
            # 假设这里是将内容保存到文件中
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Downloaded {url} to {path}")
        else:
            print(f"Failed to download {url}")

async def download_pages(url_dir):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for path, url in url_dir.items():
            tasks.append(fetch_page(session, url, path))
        await asyncio.gather(*tasks)

# 示例的url_dir
url_dir = {
    'c:\\Users\\Elysia\\Desktop\\learn\\课件\\二下\\python\\lab_2\\html_doc\\Multimodal\\Visual_Question_Answering\\Visual_Question_Answering1.html': 'https://huggingface.co/datasets?task_categories=task_categories%3Avisual-question-answering&p=1',
    'c:\\Users\\Elysia\\Desktop\\learn\\课件\\二下\\python\\lab_2\\html_doc\\Multimodal\\Visual_Question_Answering\\Visual_Question_Answering2.html': 'https://huggingface.co/datasets?task_categories=task_categories%3Avisual-question-answering&p=2',
    'c:\\Users\\Elysia\\Desktop\\learn\\课件\\二下\\python\\lab_2\\html_doc\\Multimodal\\Visual_Question_Answering\\Visual_Question_Answering3.html': 'https://huggingface.co/datasets?task_categories=task_categories%3Avisual-question-answering&p=3',
    'c:\\Users\\Elysia\\Desktop\\learn\\课件\\二下\\python\\lab_2\\html_doc\\Multimodal\\Visual_Question_Answering\\Visual_Question_Answering4.html': 'https://huggingface.co/datasets?task_categories=task_categories%3Avisual-question-answering&p=4',
    'c:\\Users\\Elysia\\Desktop\\learn\\课件\\二下\\python\\lab_2\\html_doc\\Computer_Vision\\Image_Classification\\Image_Classification1.html': 'https://huggingface.co/datasets?task_categories=task_categories%3Aimage-classification&p=1', 
    'c:\\Users\\Elysia\\Desktop\\learn\\课件\\二下\\python\\lab_2\\html_doc\\Computer_Vision\\Image_Classification\\Image_Classification2.html': 'https://huggingface.co/datasets?task_categories=task_categories%3Aimage-classification&p=2', 
    'c:\\Users\\Elysia\\Desktop\\learn\\课件\\二下\\python\\lab_2\\html_doc\\Computer_Vision\\Image_Classification\\Image_Classification3.html': 'https://huggingface.co/datasets?task_categories=task_categories%3Aimage-classification&p=3', 
}
# 运行异步下载任务
asyncio.run(download_pages(url_dir))
print('finish')