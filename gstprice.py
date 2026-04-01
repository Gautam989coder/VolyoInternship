#write a program to calulate the gst price of a product
category = input("Enter the item name[foods, electronices, medical ]")
price = float(input("Enter the price of the item: "))
if category == "foods":
    gst_price = price + (price * 0.12)
    print("The GST price of the item is: ", gst_price)  
elif category == "electronics":
    gst_price = price + (price * 0.18)
    print("The GST price of the item is: ", gst_price)
elif category == "medical":
    gst_price = price + (price * 0.05)
    print("The GST price of the item is: ", gst_price)
else:
    print("Invalid category! Please enter a valid category (foods, electronics, medical).")
