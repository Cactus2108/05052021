from django.shortcuts import render


def add_visit(request):

    if request.method == 'POST':
        pass

    return render(
        template_name='form.html',
        request=request,
    )
