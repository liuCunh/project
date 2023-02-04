class Hero:
    name = '孙悟空'
    weapon = '如意金箍棒'
    def ability(self, ability1):
        print(f'{self.name}的专属能力是：{ability1}')
print('-'*15,'欢迎来到游戏', '-'*15)
hero1 = Hero()
print('英雄1：')
print(f'姓名：{hero1.name}')
print(f'武器：{hero1.weapon}')
hero1.ability('火眼金睛')
hero2 = Hero()
hero2.name='猪八戒'
hero2.weapon='九齿钉耙'
print('英雄2：')
print(f'姓名：{hero2.name}')
print(f'武器：{hero2.weapon}')
hero2.ability('猴哥师傅被妖怪抓走了')
