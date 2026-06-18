import os
import django
from django.core.files import File
import urllib.request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TiendaMascotasWeb.settings')
django.setup()

from TiendaMascotaApp.models import Producto

products_data = [
    {
        "nombreProd": "Premium Dog Food",
        "marca": "Purina Pro Plan",
        "categoria": "Alimentos",
        "descripcion": "High-quality dog food for adult dogs.",
        "cantidad": 50,
        "precio": 45.99,
        "image_url": "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=500&q=80"
    },
    {
        "nombreProd": "Cat Tree Tower",
        "marca": "PetSafe",
        "categoria": "Accesorios",
        "descripcion": "Multi-level cat tree with scratching posts.",
        "cantidad": 15,
        "precio": 89.50,
        "image_url": "https://images.unsplash.com/photo-1543852786-1cf6624b9987?w=500&q=80"
    },
    {
        "nombreProd": "Squeaky Rubber Bone",
        "marca": "Kong",
        "categoria": "Juguetes",
        "descripcion": "Durable rubber chew toy for active dogs.",
        "cantidad": 100,
        "precio": 12.99,
        "image_url": "https://images.unsplash.com/photo-1576201836106-db1758fd1c97?w=500&q=80"
    },
    {
        "nombreProd": "Aquarium Filter",
        "marca": "Tetra",
        "categoria": "Accesorios",
        "descripcion": "Quiet and efficient filter for 20-gallon tanks.",
        "cantidad": 30,
        "precio": 25.00,
        "image_url": "https://images.unsplash.com/photo-1524704654690-b56c05c78a00?w=500&q=80"
    },
    {
        "nombreProd": "Bird Seed Mix",
        "marca": "Kaytee",
        "categoria": "Alimentos",
        "descripcion": "Nutritious blend for parakeets and small birds.",
        "cantidad": 40,
        "precio": 18.75,
        "image_url": "https://images.unsplash.com/photo-1552728089-5711db435e0c?w=500&q=80"
    }
]

def run():
    print("Clearing existing products...")
    Producto.objects.all().delete()
    
    print("Populating new products...")
    for item in products_data:
        try:
            img_url = item.pop("image_url")
            img_name = img_url.split("?")[0].split("/")[-1] + ".jpg"
            img_path = "temp_img.jpg"
            
            urllib.request.urlretrieve(img_url, img_path)
            
            producto = Producto(**item)
            with open(img_path, 'rb') as f:
                producto.foto.save(img_name, File(f), save=False)
            producto.save()
            print(f"Added product: {producto.nombreProd}")
            
            if os.path.exists(img_path):
                os.remove(img_path)
        except Exception as e:
            print(f"Failed to add {item['nombreProd']}: {e}")

if __name__ == '__main__':
    run()
    print("Database populated successfully.")
