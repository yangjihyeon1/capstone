from django.shortcuts import render
from .pdf_summarizer import extract_text_from_pdf
import trafilatura

def extract_text_from_url(url):
    """
    trafilatura를 이용해 URL에서 기사 본문 텍스트를 정확하게 추출
    """
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            return "URL에서 페이지를 가져오지 못했습니다."
        text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
        if not text or len(text.strip()) == 0:
            return "본문을 추출하지 못했습니다."
        return text.strip()
    except Exception as e:
        return f"기사 크롤링 실패: {e}"


def home(request):
    summary = ""

    if request.method == "POST":
        # PDF 업로드 처리
        uploaded_file = request.FILES.get('pdf_file')
        if uploaded_file:
            temp_path = f'temp_{uploaded_file.name}'
            with open(temp_path, 'wb+') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)
            text = extract_text_from_pdf(temp_path)
            summary = text[:2000]  # 미리보기용 (앞 2000자만)

        # URL 입력 처리
        url = request.POST.get('url_input')
        if url:
            text = extract_text_from_url(url)
            summary = text[:2000]

    return render(request, 'summaryapp/index.html', {'summary': summary})
