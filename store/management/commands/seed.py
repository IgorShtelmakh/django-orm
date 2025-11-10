# store/management/commands/seed.py
from django.core.management.base import BaseCommand
from store.models import Category, Supplier, Product, Customer, CustomerAddress, Order, OrderItem, Payment, Shipment
from decimal import Decimal
from django.utils import timezone
import random


class Command(BaseCommand):
    help = 'Наповнення бази даних демонстраційними даними'

    def handle(self, *args, **kwargs):
        self.stdout.write('Початок наповнення БД...')

        # Очищення даних (опціонально)
        self.stdout.write('Очищення існуючих даних...')
        Shipment.objects.all().delete()
        Payment.objects.all().delete()
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        CustomerAddress.objects.all().delete()
        Customer.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Supplier.objects.all().delete()

        # Створення категорій
        self.stdout.write('Створення категорій...')
        categories_data = [
            {'name': 'Ноутбуки'},
            {'name': 'Смартфони'},
            {'name': 'Телевізори'},
            {'name': 'Побутова техніка'},
            {'name': 'Аудіотехніка'},
            {'name': 'Комп\'ютери'},
            {'name': 'Планшети'},
            {'name': 'Аксесуари'},
        ]
        categories = []
        for cat_data in categories_data:
            cat = Category.objects.create(**cat_data)
            categories.append(cat)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(categories)} категорій'))

        # Створення постачальників
        self.stdout.write('Створення постачальників...')
        suppliers_data = [
            {'name': 'TechSupplier Inc', 'phone': '+380501234567', 'email': 'info@techsupplier.com'},
            {'name': 'ElectroWorld', 'phone': '+380502345678', 'email': 'sales@electroworld.com'},
            {'name': 'SmartDevices Co', 'phone': '+380503456789', 'email': 'contact@smartdevices.com'},
            {'name': 'HomeAppliances Ltd', 'phone': '+380504567890', 'email': 'info@homeappliances.com'},
            {'name': 'AudioPro', 'phone': '+380505678901', 'email': 'sales@audiopro.com'},
        ]
        suppliers = []
        for supp_data in suppliers_data:
            supp = Supplier.objects.create(**supp_data)
            suppliers.append(supp)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(suppliers)} постачальників'))

        # Створення товарів
        self.stdout.write('Створення товарів...')
        products_data = [
            {'sku': 'LAP001', 'name': 'Ноутбук ASUS VivoBook', 'category': categories[0], 'default_supplier': suppliers[0], 'list_price': Decimal('25000.00'), 'discount': Decimal('5.00'), 'description': 'Потужний ноутбук для роботи та навчання'},
            {'sku': 'LAP002', 'name': 'MacBook Pro 14"', 'category': categories[0], 'default_supplier': suppliers[0], 'list_price': Decimal('85000.00'), 'discount': Decimal('0.00'), 'description': 'Професійний ноутбук від Apple'},
            {'sku': 'LAP003', 'name': 'Lenovo ThinkPad', 'category': categories[0], 'default_supplier': suppliers[0], 'list_price': Decimal('32000.00'), 'discount': Decimal('10.00'), 'description': 'Бізнес-ноутбук з високою надійністю'},
            {'sku': 'PHO001', 'name': 'iPhone 15 Pro', 'category': categories[1], 'default_supplier': suppliers[2], 'list_price': Decimal('45000.00'), 'discount': Decimal('0.00'), 'description': 'Новітній флагманський смартфон'},
            {'sku': 'PHO002', 'name': 'Samsung Galaxy S24', 'category': categories[1], 'default_supplier': suppliers[2], 'list_price': Decimal('38000.00'), 'discount': Decimal('5.00'), 'description': 'Топовий Android смартфон'},
            {'sku': 'PHO003', 'name': 'Xiaomi 14', 'category': categories[1], 'default_supplier': suppliers[2], 'list_price': Decimal('22000.00'), 'discount': Decimal('15.00'), 'description': 'Смартфон з найкращим співвідношенням ціна/якість'},
            {'sku': 'TV001', 'name': 'Samsung QLED 55"', 'category': categories[2], 'default_supplier': suppliers[1], 'list_price': Decimal('42000.00'), 'discount': Decimal('8.00'), 'description': '4K Smart TV з квантовими точками'},
            {'sku': 'TV002', 'name': 'LG OLED 65"', 'category': categories[2], 'default_supplier': suppliers[1], 'list_price': Decimal('78000.00'), 'discount': Decimal('0.00'), 'description': 'Преміум OLED телевізор'},
            {'sku': 'APP001', 'name': 'Пральна машина Bosch', 'category': categories[3], 'default_supplier': suppliers[3], 'list_price': Decimal('18000.00'), 'discount': Decimal('12.00'), 'description': 'Автоматична пральна машина 8 кг'},
            {'sku': 'AUD001', 'name': 'Sony WH-1000XM5', 'category': categories[4], 'default_supplier': suppliers[4], 'list_price': Decimal('12000.00'), 'discount': Decimal('0.00'), 'description': 'Бездротові навушники з активним шумозаглушенням'},
        ]
        products = []
        for prod_data in products_data:
            prod = Product.objects.create(**prod_data)
            products.append(prod)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(products)} товарів'))

        # Створення клієнтів
        self.stdout.write('Створення клієнтів...')
        customers_data = [
            {'first_name': 'Іван', 'last_name': 'Петренко', 'email': 'ivan.petrenko@example.com', 'phone': '+380671234567'},
            {'first_name': 'Марія', 'last_name': 'Коваленко', 'email': 'maria.kovalenko@example.com', 'phone': '+380672345678'},
            {'first_name': 'Олександр', 'last_name': 'Шевченко', 'email': 'oleksandr.shevchenko@example.com', 'phone': '+380673456789'},
            {'first_name': 'Оксана', 'last_name': 'Мельник', 'email': 'oksana.melnyk@example.com', 'phone': '+380674567890'},
            {'first_name': 'Дмитро', 'last_name': 'Бондаренко', 'email': 'dmytro.bondarenko@example.com', 'phone': '+380675678901'},
        ]
        customers = []
        for cust_data in customers_data:
            cust = Customer.objects.create(**cust_data)
            customers.append(cust)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(customers)} клієнтів'))

        # Створення адрес клієнтів
        self.stdout.write('Створення адрес клієнтів...')
        addresses = []
        cities = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро']
        streets = ['вул. Хрещатик', 'вул. Шевченка', 'вул. Франка', 'вул. Бандери', 'вул. Грушевського']
        for customer in customers:
            # Shipping address
            addr = CustomerAddress.objects.create(
                customer=customer,
                address_type='shipping',
                street=f'{random.choice(streets)}, {random.randint(1, 100)}',
                city=random.choice(cities),
                postal_code=f'{random.randint(10000, 99999)}',
                country='Україна'
            )
            addresses.append(addr)
            # Billing address
            addr = CustomerAddress.objects.create(
                customer=customer,
                address_type='billing',
                street=f'{random.choice(streets)}, {random.randint(1, 100)}',
                city=random.choice(cities),
                postal_code=f'{random.randint(10000, 99999)}',
                country='Україна'
            )
            addresses.append(addr)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(addresses)} адрес'))

        # Створення замовлень
        self.stdout.write('Створення замовлень...')
        orders = []
        statuses = ['pending', 'processing', 'shipped', 'delivered']
        for i, customer in enumerate(customers):
            shipping_addr = CustomerAddress.objects.filter(customer=customer, address_type='shipping').first()
            # Створюємо 1-3 замовлення на клієнта
            for j in range(random.randint(1, 3)):
                order = Order.objects.create(
                    customer=customer,
                    status=random.choice(statuses),
                    shipping_address=shipping_addr,
                    total_amount=Decimal('0.00')  # буде оновлено пізніше
                )
                orders.append(order)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(orders)} замовлень'))

        # Створення позицій замовлення
        self.stdout.write('Створення позицій замовлення...')
        order_items = []
        for order in orders:
            # Додаємо 1-4 товари до кожного замовлення
            order_total = Decimal('0.00')
            num_items = random.randint(1, 4)
            selected_products = random.sample(products, num_items)
            for product in selected_products:
                quantity = random.randint(1, 3)
                item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    unit_price=product.list_price
                )
                order_items.append(item)
                order_total += item.get_total()
            # Оновлюємо загальну суму замовлення
            order.total_amount = order_total
            order.save()
        self.stdout.write(self.style.SUCCESS(f'Створено {len(order_items)} позицій замовлення'))

        # Створення платежів
        self.stdout.write('Створення платежів...')
        payments = []
        payment_methods = ['cash', 'card', 'bank_transfer', 'online']
        payment_statuses = ['pending', 'completed', 'failed']
        for order in orders:
            payment = Payment.objects.create(
                order=order,
                amount=order.total_amount,
                payment_method=random.choice(payment_methods),
                status=random.choice(payment_statuses),
                transaction_id=f'TRX{random.randint(100000, 999999)}'
            )
            payments.append(payment)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(payments)} платежів'))

        # Створення відправлень (для деяких замовлень)
        self.stdout.write('Створення відправлень...')
        shipments = []
        carriers = ['Нова Пошта', 'Укрпошта', 'Meest', 'Justin']
        shipment_statuses = ['pending', 'in_transit', 'delivered']
        # Створюємо відправлення лише для частини замовлень
        for order in random.sample(orders, min(len(orders), len(orders) // 2)):
            shipment = Shipment.objects.create(
                order=order,
                carrier=random.choice(carriers),
                tracking_number=f'TN{random.randint(100000000, 999999999)}',
                status=random.choice(shipment_statuses)
            )
            shipments.append(shipment)
        self.stdout.write(self.style.SUCCESS(f'Створено {len(shipments)} відправлень'))

        self.stdout.write(self.style.SUCCESS('База даних успішно наповнена!'))
        self.stdout.write(f'Загальна статистика:')
        self.stdout.write(f'  - Категорій: {Category.objects.count()}')
        self.stdout.write(f'  - Постачальників: {Supplier.objects.count()}')
        self.stdout.write(f'  - Товарів: {Product.objects.count()}')
        self.stdout.write(f'  - Клієнтів: {Customer.objects.count()}')
        self.stdout.write(f'  - Адрес: {CustomerAddress.objects.count()}')
        self.stdout.write(f'  - Замовлень: {Order.objects.count()}')
        self.stdout.write(f'  - Позицій замовлення: {OrderItem.objects.count()}')
        self.stdout.write(f'  - Платежів: {Payment.objects.count()}')
        self.stdout.write(f'  - Відправлень: {Shipment.objects.count()}')
