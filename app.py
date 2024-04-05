import streamlit as st

def calculate_price(preparation_minutes, tattooing_minutes, in_shop_minutes, friend_discount, loyal_customer_discount):
    preparation_rate = 62.5 / 60  # $50 per hour
    tattooing_rate = 150 / 60  # $100 per hour
    in_shop_rate = 32.5 / 60  # $30 per hour for time spent in shop without tattooing
    
    # Calculate costs for each type of time spent
    preparation_cost = preparation_minutes * preparation_rate
    tattooing_cost = tattooing_minutes * tattooing_rate
    in_shop_cost = in_shop_minutes * in_shop_rate
    
    # Apply discounts
    total_cost = preparation_cost + tattooing_cost + in_shop_cost
    if friend_discount:
        total_cost *= 0.8  # Apply a 20% discount
    elif loyal_customer_discount:
        total_cost *= 0.9  # Apply a 10% discount
    
    return total_cost

st.title('Tattoo Price Calculator')

prep_time = st.number_input('Preparation time (minutes)', min_value=0, value=30)
tattoo_time = st.number_input('Tattooing time (minutes)', min_value=0, value=60)
in_shop_time = st.number_input('Time in shop (minutes)', min_value=0, value=30)

friend_discount = st.checkbox('Apply Friend Discount (20%)')
loyal_customer_discount = st.checkbox('Apply Loyal Customer Discount (10%)')

if st.button('Calculate Total Price'):
    if friend_discount and loyal_customer_discount:
        st.write("Please select only one discount option.")
    else:
        price = calculate_price(prep_time, tattoo_time, in_shop_time, friend_discount, loyal_customer_discount)
        st.write(f"The total price is €{price:.2f}")
