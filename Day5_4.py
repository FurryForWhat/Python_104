a = ['1','add','1','4','10','3.11','zero']
print(a[5])
print(a.index('add'))
# print(a[4].isdigit())
a.append('hi')
print(a)
a.insert(0,'2')
# print(a)
a.pop(1)
print(a)

# index number 5 မှာရှိတဲ့ ဒေတာကိုထုတ်မယ်   3.11
# 'add'  ဆိုတဲ့ dataရဲ့ indexကို ထုတ်မယ်     1
#index number 4 မှာ intဖြစ်မဖြစ်ကို စစ်မယ်။  True
#နောက်ဆုံးအခန်းမှာ 'hi'ဆိုတဲ့ dataထည့်မယ်။   ['1','add',1,4,10,3.11,'zero','hi']
#index 0 မှာ '1'ကို '2' ပြောင်းမယ်။        ['2','add',1,4,10,3.11,'zero','hi']