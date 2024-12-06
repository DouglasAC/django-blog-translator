from django.shortcuts import render

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        print(original_text)
        return render(request, 'translator.html', {'output_text': original_text, 'original_text': original_text})
    else:    
        return render(request, 'translator.html')