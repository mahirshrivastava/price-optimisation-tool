from ..models.product_model import Products
from ..models.user_model import Users, db
from ..shared.custom_exception import AuthorizationException, InvalidParameterException


def fetch_product(product_id, email):
    """Fetch product via product id"""
    user = Users.query.filter_by(email=email).first_or_404()
    product = Products.query.filter_by(id=product_id).first_or_404()
    if user.id != product.user_id:
        raise AuthorizationException()
    serialized_product = serialize_product(product)
    return serialized_product


def fetch_product_list(email):
    """Fetch product list"""
    user = Users.query.filter_by(email=email).first_or_404()
    products = Products.query.all()
    serialized_product_list = []
    for product in products:
        serialized_product_list.append(serialize_product(product))
    return serialized_product_list


def register_product(payload):
    """Register product"""
    product = Products(
        product_name=(payload.product_name).capitalize(),
        description=(payload.description).capitalize(),
        cost_price=payload.cost_price,
        selling_price=payload.selling_price,
        category=(payload.category).capitalize(),
        stock_available=payload.available_stock,
        units_sold=payload.units_sold,
        customer_rating=payload.customer_rating,
        demand_forecast=payload.demand_forecast,
        optimized_price=payload.optimized_price,
    )
    db.session.add(product)
    db.session.commit()
    return "Product created!"


def update_product(payload, validated_payload, product_id):
    """Updating product"""
    product = Products.query.filter_by(id=product_id).first_or_404()
    if "description" in payload:
        product.description = validated_payload.description
    if "cost_price" in payload:
        product.cost_price = validated_payload.cost_price
    if "selling_price" in payload:
        product.selling_price = validated_payload.selling_price
    if "category" in payload:
        product.category = validated_payload.category
    if "stock_available" in payload:
        product.stock_available = validated_payload.stock_available
    if "units_sold" in payload:
        product.units_sold = validated_payload.units_sold
    if "customer_rating" in payload:
        product.customer_rating = validated_payload.customer_rating
    if "demand_forecast" in payload:
        product.demand_forecast = validated_payload.demand_forecast
    if "optimized_price" in payload:
        product.optimized_price = validated_payload.optimized_price
    db.session.commit()
    return "Product Updated"


def delete_product(product_id):
    """Deleting product"""
    products = Products.query.filter_by(id=product_id).first_or_404()
    if not products:
        raise InvalidParameterException(message="Invalid product id!")
    db.session.delete(products)
    db.session.commit()
    return "Product deleted!"


def calculated_demand_forecast(payload):
    """Calculating demand forecast"""
    product_ids = [product_id for product_id in payload]
    products = Products.query.filter(Products.id.in_(product_ids)).all()
    if products:
        optimized_product = []
        for product in products:
            base_demand = product.units_sold
            price_factor = product.cost_price / product.selling_price
            rating_factor = 1 + (product.customer_rating / 5) * 0.5
            stock_factor = min(1, product.stock_available / max(product.units_sold, 1))
            demand_forecast = int(
                base_demand * price_factor * rating_factor * stock_factor
            )
            product.demand_forecast = demand_forecast
            optimized_product.append(serialize_product(product))
        return optimized_product
    else:
        raise InvalidParameterException("No product found!", code=404)


def calculate_optimized_price():
    """Calculate optimized price"""
    products = Products.query.all()
    if products:
        optimized_product = []
        for product in products:
            cost_price = product.cost_price
            selling_price = product.selling_price
            available_stock = product.stock_available
            units_sold = product.units_sold
            demand_ratio = (units_sold + 1) / (available_stock + 1)
            if demand_ratio > 0.5:
                adjustment = selling_price * 0.10
            elif demand_ratio < 0.2:
                adjustment = -selling_price * 0.10
            else:
                adjustment = 0
            optimized_price = selling_price + adjustment
            min_price = cost_price * 1.10
            optimized_price = round(max(optimized_price, min_price), 2)
            product.optimized_price = optimized_price
            optimized_product.append(serialize_product(product))
        return optimized_product
    else:
        raise InvalidParameterException("No product found!", code=404)


def serialize_product(product_object):
    """Serializing products"""
    return {
        "id": product_object.id,
        "product_name": product_object.product_name,
        "description": product_object.description,
        "cost_price": product_object.cost_price,
        "selling_price": product_object.selling_price,
        "category": product_object.category,
        "available_stock": product_object.stock_available,
        "units_sold": product_object.units_sold,
        "customer_rating": product_object.customer_rating,
        "demand_forecast": product_object.demand_forecast,
        "optimized_price": product_object.optimized_price,
    }
