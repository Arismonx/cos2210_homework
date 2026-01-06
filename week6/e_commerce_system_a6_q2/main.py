from ecommerce.cart import add_item, remove_item, calculate_total, apply_discount

cart = []

print("--- เริ่มการช้อปปิ้ง ---")
add_item(cart, "Mouse", 500)
add_item(cart, "Keyboard", 1500)
add_item(cart, "Monitor", 4000)

print("เพิ่ม Mouse ราคา 500 บาท")
print("เพิ่ม Keyboard ราคา 1500 บาท")
print("เพิ่ม Monitor ราคา 4000 บาท")


print("--- เปลี่ยนใจ ---")
remove_item(cart, "Mouse")
print("ลบ Mouse ออกแล้ว")

print("--- สรุปยอด ---")
total = calculate_total(cart)
print(f"ราคารวม: {total} บาท")
print(f"ราคาหลังหักส่วนลด 10%: {apply_discount(total,10)} บาท")
