# 类中方法
# 种类： 普通方法、 类方法、静态方法、魔术方法
"""
普通方法：
    def 方法名(self[, 参数，...]):
        方法体

"""


class Phone:
    brand = 'XiaoMi'
    prince = 4999
    type = 'Mate 80'

    # Phone里面的方法
    def call(self):
        # print(f'self------>{self}')
        print(f'正在访问通讯录：')
        for person in self.address_book:
            print(person.items())
        print(f'正在打电话！！！')
        print(f'留言：{self.note}')


phone1 = Phone()
phone1.note = '我的电话一的note'
phone1.address_book = [{"110": 'Tome', "120": "Jury", "119": "Lucy"}]
print(phone1, 1)
# print(phone1.brand, 2)
phone1.call()  # call(phone1) -->self.note

print('-' * 30)
phone2 = Phone()
phone2.note = '我点电话二的note'
print(phone2)
phone2.call()  # call(phone2) -->self.note
