from django.shortcuts import render, redirect
from django.urls import reverse


class ObjectCreateMixin:
    model_form = None
    template = None
    redirect_url = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST, request.FILES)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)

        context = {
            self.model.__name__.lower(): obj,
            'form': bound_form
        }
        return render(request, self.template, context=context)

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, request.FILES, instance=obj)

        if bound_form.is_valid():
            updated_obj = bound_form.save()
            return redirect(updated_obj)

        context = {
            self.model.__name__.lower(): obj,
            'form': bound_form
        }
        return render(request, self.template, context=context)


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
