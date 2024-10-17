from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)

def buyItem(request, id):
    object = Product.objects.get(id = id)
    object.update(new_q = object.quantity+1)
    object.save()
    print(object.quantity)

    products = Product.objects.all()
    context = {'products': products}
    return HttpResponse(f'Спасибо за покупку!')

"""     obj = objects.objects.filter(pk = 2)
    for ob in objects:
        if ob['id'] == id:
            if ob['quantity'] > 0:
                ob['quantity'] -= 1
                objects.update()
                products = Product.objects.all()
                print(objects[4]['quantity'])
                products = Product.objects.all()
                context = {'products': products}
                return render(request, 'shop/index.html', context)
            else:
                return render(request, './purhcase_error.html')
    return render(request, './purhcase_error.html') """

class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        print(self.object.product)
        object = Product.objects.get(id = self.object.product.id)
        if (object.quantity == 0):
            return render('', 'shop/purhcase_error.html')
        object.update(new_q = object.quantity-1)
        object.save()
        print(object.quantity)

        products = Product.objects.all()
        context = {'products': products}
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')