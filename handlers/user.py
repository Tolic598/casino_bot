from aiogram import Dispatcher, types, Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from typing import Any, Dict
from aiogram.filters.command import Command
from aiogram.handlers import CallbackQueryHandler
import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard.inline import slots, canal
from keyboard.keyboard import menu
import time
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pymysql
from pymysql.cursors import DictCursor
import pymysql.cursors
from config import host, user, password, db_name

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
start_time = time.time()

dt = datetime.datetime.today().strftime('%d.%m %H:%M')
end_time = (time.time()) - start_time

print((f'Бот запущен\nДата запуска: {dt}\nВремя запуска: {round(end_time,1)} секунды\n'))

try:
    connection = pymysql.connect(host = host,
                                user = user,
                                password = password,
                                database = db_name,
                                charset='utf8mb4',
                                port=3306,
                                cursorclass=DictCursor)
except Exception as ex:
    print(ex)

router = Router()

class statistics(StatesGroup):
    suma = State()
    rate = State()
    prom = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext, bot):
    id = message.from_user.id
    suma = 0
    rate = 0
    prom = 0
    pr_1 = 0
    pr_2 = 0
    pr_3 = 0
    pr_4 = 0
    pr_5 = 0
    pr_6 = 0
    pr_7 = 0
    pr_8 = 0
    pr_9 = 0
    pr_10 = 0
    pr_11 = 0
    pr_12 = 0
    pr_13 = 0
    pr_14 = 0
    pr_15 = 0
    pr_16 = 0
    pr_17 = 0
    pr_18 = 0
    pr_19 = 0
    pr_20 = 0
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id=%s",(id))
        if cursors.rowcount == 1:
            await message.answer("Введите сумму депозита в виде числа:")
            await state.set_state(statistics.suma)
        elif cursors.rowcount == 0:
            chat_member = await bot.get_chat_member('@searchslot',id)
            if chat_member.status == 'member' or chat_member.status == 'administrator' or chat_member.status == 'creator':
                cursors.execute('''INSERT IGNORE INTO users (id,suma,rate,prom,pr_1,pr_2,pr_3,pr_4,pr_5,pr_6,pr_7,pr_8,pr_9,pr_10,pr_11,pr_12,pr_13,pr_14,pr_15,pr_16,pr_17,pr_18,pr_19,pr_20)
                    VALUES(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)''' % (int(id),int(suma),int(rate),int(prom),int(pr_1),int(pr_2),int(pr_3),int(pr_4),int(pr_5),int(pr_6),int(pr_7),int(pr_8),int(pr_9),int(pr_10),int(pr_11),int(pr_12),int(pr_13),int(pr_14),int(pr_15),int(pr_16),int(pr_17),int(pr_18),int(pr_19),int(pr_20)))
                await message.answer("Введите сумму депозита в виде числа:")
                await state.set_state(statistics.suma)
                setup(bot,id)
            else:
                await message.answer("Вcтупите в наш канал для просмотра статистики и новостей", reply_markup=canal)
    connection.commit()

#Проверить подписку
@router.callback_query(F.data == 'check')
async def check(call: types.CallbackQuery, state: FSMContext, bot):
    id = call.from_user.id
    suma = 0
    rate = 0
    prom = 0
    pr_1 = 0
    pr_2 = 0
    pr_3 = 0
    pr_4 = 0
    pr_5 = 0
    pr_6 = 0
    pr_7 = 0
    pr_8 = 0
    pr_9 = 0
    pr_10 = 0
    pr_11 = 0
    pr_12 = 0
    pr_13 = 0
    pr_14 = 0
    pr_15 = 0
    pr_16 = 0
    pr_17 = 0
    pr_18 = 0
    pr_19 = 0
    pr_20 = 0
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id=%s",(id))
        if cursors.rowcount == 1:
            await call.message.answer(f'Введите сумму депозита в виде числа:')
            await state.set_state(statistics.suma)
        elif cursors.rowcount == 0:
            chat_member = await bot.get_chat_member('@botfazzer',id)
            if chat_member.status == 'member' or chat_member.status == 'administrator' or chat_member.status == 'creator':
                cursors.execute('''INSERT IGNORE INTO users (id,suma,rate,prom,pr_1,pr_2,pr_3,pr_4,pr_5,pr_6,pr_7,pr_8,pr_9,pr_10,pr_11,pr_12,pr_13,pr_14,pr_15,pr_16,pr_17,pr_18,pr_19,pr_20)
                    VALUES(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)''' % (int(id),int(suma),int(rate),int(prom),int(pr_1),int(pr_2),int(pr_3),int(pr_4),int(pr_5),int(pr_6),int(pr_7),int(pr_8),int(pr_9),int(pr_10),int(pr_11),int(pr_12),int(pr_13),int(pr_14),int(pr_15),int(pr_16),int(pr_17),int(pr_18),int(pr_19),int(pr_20)))
                await call.message.answer(f'Введите сумму депозита в виде числа:')
                await state.set_state(statistics.suma)
                setup(bot,id)
                await call.message.delete()
            else:
                await call.message.answer(f'Вcтупите в наш канал для просмотра статистики и новостей', reply_markup=canal)
                await call.message.delete()
    connection.commit()

@router.message(statistics.suma)
async def process_name(message: Message, state: FSMContext):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await state.update_data(suma=message.text)
    suma = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"UPDATE users SET suma = {suma} WHERE id = {id}")
        if suma.isdigit():
            await message.answer(f"Ваша сумма депозита: {suma}\nМы не несём ответственность за ваши средства!!!", reply_markup=menu)
            await state.clear()
        else:
            await message.answer("Введите сумму депозита в виде числа:")
            await state.set_state(statistics.suma)
    connection.commit()

@router.message(F.text == "Слоты")
async def profil(message: Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Выберете провайдер:", reply_markup=slots)

@router.message(F.text == "Профиль")
async def profil(message: Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Привет {name}, выберете провайдер,а бот вам выберет слот", reply_markup=slots)

@router.message(F.text == "Статистика")
async def profil(message: Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        for row in cursors:
            pr_1 = row['pr_1']
            pr_2 = row['pr_2']
            pr_3 = row['pr_3']
            pr_4 = row['pr_4']
            pr_5 = row['pr_5']
            pr_6 = row['pr_6']
            pr_7 = row['pr_7']
            pr_8 = row['pr_8']
            pr_9 = row['pr_9']
            pr_10 = row['pr_10']
            pr_11 = row['pr_11']
            pr_12= row['pr_12']
            pr_13 = row['pr_13']
            pr_14 = row['pr_14']
            pr_15 = row['pr_15']
            pr_16 = row['pr_16']
            await message.answer(f"Вот статистика по провайдерам в которые вы играли:\n3 Oaks Gaming: {pr_1}\nPragmaticPlay: {pr_2}\nBetSoft: {pr_3}\nRed Tiger: {pr_4}\nBig Time Gaming: {pr_5}\nRelax Gaming: {pr_6}\nPlay'n GO: {pr_7}\nPlayson: {pr_8}\nWazdan: {pr_9}\nAmatic: {pr_10}\nYggdrasil: {pr_11}\nNolimitCity: {pr_12}\nBGaming: {pr_13}\nEndorphina: {pr_14}\nQuickspin: {pr_15}\nHabanero: {pr_16}", reply_markup=menu)

@router.message(F.text == "Поддержать проект")
async def profil(message: Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Я буду рад вашей поддержке, все ваши донаты пойдут на развитие проекта и хостинг\nBinance pay: <code>294638367</code>\nUSDT сеть: Tron(TRC20): <code>TNr1U4DkWhR56B5sPh5AVBqszdtu4vyFrY</code>\n\nПишите мне в личное сообщение чтоб вы хотели увидеть в боте @codefarm ",reply_markup=menu, parse_mode='html')

#3 Oaks Gaming
@router.callback_query(F.data == 'btn1')
async def btn1(call: types.CallbackQuery, state: FSMContext):
    my_list_okks3 = ['SUN OF EGYPT 4', 'AZTEC FIRE 2', 'GOLD NUGGETS', 'OLAF VIKING', 'CRYSTAL SCARABS', 'GRAB MORE GOLD!', 'AFRICAN SPIRIT STICKY WILDS', '3 HOT CHILLIES', '777 COINS', 'Black Wolf 2', 'Little Farm', 'Green Chilli 2', 'FOREST SPIRIT', 'COIN VOLCANO', 'LADY FORTUNE', 'MUMMY POWER', 'TIGER GEMS', 'GRAB THE GOLD!', 'MORE MAGIC APPLE', 'EGYPT FIRE', 'YO-HO GOLD!', 'MAYA SUN', 'BOOM! BOOM! GOLD!', 'DRAGON WEALTH', 'SUNLIGHT PRINCESS', 'GODDESS OF EGYPT', 'RIO GEMS', 'HIT MORE GOLD!', 'STICKY PIGGY', 'GREEN CHILLI', 'BIG HEIST', 'AZTEC FIRE', 'LOTUS CHARM', 'EGGS OF GOLD', 'MAGIC APPLE 2', 'CAISHEN WEALTH', 'SUN OF EGYPT 3', 'PEARL DIVER 2: TREASURE CHEST', 'FISH REEF', 'QUEEN OF THE SUN', 'BOOK OF WIZARD: CRYSTAL CHANCE', 'BUDDHA MEGAWAYS', 'BLACK WOLF', 'CANDY BOOM', 'GOLD EXPRESS', 'LORD FORTUNE 2', 'BOOK OF WIZARD', 'TIGER JUNGLE', 'WOLF NIGHT', '3 COINS: EGYPT', 'PEARL DIVER', 'WUKONG', 'SCARAB BOOST', 'HIT THE GOLD!', 'AZTEC PYRAMID', 'MAGIC BALL: MULTICHANCE', 'MAGIC APPLE', 'SUPER RICH GOD', 'WOLF SAGA', '3 COINS', 'EYE OF GOLD', 'TIGER STONE', 'SUN OF EGYPT 2', 'SCARAB TEMPLE', 'THUNDER OF OLYMPUS', '15 DRAGON PEARLS', 'BUDDHA FORTUNE', 
    'SUPER MARBLE', 'AZTEC SUN', 'MOON SISTERS', 'BOOK OF SUN: CHOICE', 'GREAT PANDA', "TIGER'S GOLD", '777 GEMS RESPIN', 'SUN OF EGYPT', 'SCARAB RICHES', 'OLYMPIAN GODS', 'BOOK OF SUN: MULTICHANCE', 'DRAGON PEARLS', 'BOOK OF SUN']
    random_my_list_okks3 = random.choice(my_list_okks3)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: 3 Oaks Gaming\nСлот: <code>{random_my_list_okks3}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn1_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_1 = pr_1 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_1 = pr_1 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера 3 Oaks Gaming
@router.callback_query(F.data == 'del1')
async def del1(call: types.CallbackQuery):
    button_number = int('del1'[3:])
    button_number_1 = int('btn1'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: 3 Oaks Gaming',reply_markup=slots)
    await call.message.delete()

#PragmaticPlay
@router.callback_query(F.data == 'btn2')
async def btn2(call: types.CallbackQuery, state: FSMContext):
    my_list_pragmat = ['Castle of Fire', 'The Big Dawgs', 'Blade & Fangs', 'Gates of Olympus 1000', 'Gates of Xibalba', 'Juicy Fruits Multihold', 'Fire Stampede', 'Floating Dragon New Year Festival Ultra Megaways Hold & Spin', 'Cyber Heist', 'Mr TainвЂ™s Fishing Adventures', 'Sea Fantasy', 'Candy Jar Clusters', 'Ding Dong Christmas Bells', 'Xmas Spark', 'Rise of Samurai IV', 'Sugar Rush Xmas', '5 Frozen Charms', 'Big Bass Christmas Bash', 'The Wild Gang', 'Nile Fortunes', 
    'Chase for Glory', 'Timber Stacks', 'Sugar Supreme Powernudge', 'Mahjong X', 'Rujak Bonanza', 'Viking Forge', 'The Money Men Megaways', 'Gemine', 'John Hunter NellвЂ™Antica Roma', 'Big Bass Halloween', '888 Bonanza', 'Infective Wild', 'TundraвЂ™s Fortune', 'Cash Chips', 'Demon Pots', 'Twilight Princess', 'Gravity Bonanza', 'Mr Toad Gold Megaways', 'Rainbow Reels', 'Gold Oasis', 'Mahjong Wins', 'Starlight Princess 1000', 'Gemstone', '8 Golden Dragon Challenge', 'Fortunes of the Aztec', 'Book of Tut Megaways', 'Yi Sun Shin', 'Frozen Tropics', 'Saiyan Mania', 'Racing Joker', 'Candy Blitz', 'Cyclops Smash', 'Tucanito', 'Big Bass Hold & Spin Megaways', 'Mustang Trail', 'Forge of Olympus', 'Pub Kings', 'Piggy Bankers', 'Rocket Blast Megaways', 'Supermania', 'Diamond Cascade', 'Frogs & Bugs', 'Sky Bounty', 'Lobster BobвЂ™s Crazy Crab Shack', '3 Buzzing Wilds', 'Cash Box', 'Power of Merlin Megaways', 'Hellvis Wild',
    'LadyBug Luck', 'Spellbinding Mystery', 'Wisdom of Athena', 'Oishii Bonanza', 'Heist for the Golden Nuggets', 'Big Bass Amazon Xtreme', 'Fat Panda', 'Robber Strike', 'Country Farming', 'Floating Dragon вЂ“ Dragon Boat Festival', 'Pirates Pub', 'Via Del Corso', 'Sticky Bees', 'Zeus vs Hades вЂ“ Gods of War', 'Joker Blast Bonanza', 'Jewel Rush', 'Hockey Bonanza', 'Lamp Of Infinity', 'Madame Mystique Megaways', 'Sugar Twist', 'Diamonds Of Egypt', 'Knight Hot Spotz', 'Wild Bison Charge', 'Excalibur Unleashed', 'Slushie Party', 'Kingdom of The Dead', 'Jane Hunter and the Mask of Montezuma', '3 Dancing Monkeys', 'Wild Celebrity Bus Megaways', 'Moonshot', 'African Elephant', 'Guarana Eyes of the Amazon', 'Gods of Giza', 'The Red Queen', 'Gates of Hades', 'Big Bass Bonanza вЂ“ Hold & Spinner', 'Grace of Ebisu', 'The Dog House Multihold', 'Rabbit Garden', 'Wild West Duels', 'The Knight King', 'Jasmine Dreams', 'Mochimon', 'Cowboy Coins', 'Gatot KacaвЂ™s Fury', 'Flying Hippo', 'Mystery of the Orient', 'Wild Wild Riches Megaways', 'Peak Power', 'Club Tropicana', 'Fire Archer', 'Gates of Aztec', 'Monster Superlanche', 'The Dog House Dice Show', 'Fish Eye', 'Mammoth Gold Megaways', 'Secret City Gold', 'Pinup Girls', 'JokerвЂ™s Jewels Dice', 'Sweet Bonanza Dice', 'Wild Wild Bananas', 'Dragon Hero', '5 Rabbits Megaways', 'The Tweety House', 'Lucky Fishing Megaways', 'Gates of Gatot Kaca', 'Sweet Powernudge', 'PIZZA! PIZZA? PIZZA!', 'Hot Pepper', 'Starlight Christmas', 'Reel Banks', 'Fury of Odin Megaways', 'Sweet Fiesta', 'Bigger Bass Blizzard вЂ“ Christmas Catch', 'Lucky Phoenix Megaways', 'SantaвЂ™s Great Gifts', 'Bison Spirit', 'Kingdom of Asgard', 'Snakes & Ladders Snake Eyes', 'Gems of Serengeti', 'Jewel Bonanza', 'Firebird Spirit', 'Towering Fortunes', 'Old Gold Miner Megaways', 'Pirate Golden Age', 'Spin & Score Megaways', 'John Hunter and the Book of Tut Respin', 'Release the Kraken 2', 'The Dog Mansion Megaways', 'Sword of Ares', 'Big Bass вЂ“ Keeping it Reel', 'Candy Stars', 'Legend of Heroes Megaways', 'Shield of Sparta', 'Muertos Multiplier Megaways', 'Aztec Blaze', 'Wildman Super Bonanza', 'Floating Dragon Megaways', 'Wild Hop&Drop', 'Crown of Fire', 'Book of Golden Sands', 'Striking Hot 5', 'Coffee Wild', 'Happy Hooves', 'Pyramid Bonanza', 'Octobeer Fortunes', 'Fire Hot 100', 'Fire Hot 20', 'Fire Hot 40', 'Fire Hot 5', 'Down the Rails', 'Hot to Burn Extreme', 'Black Bull', 'Greedy Wolf', 'Gorilla Mayhem', 'Mahjong Panda', 'Magic Money Maze', 'Tropical Tiki', 'Wolf Gold Power Jackpot', 'Shining Hot 100', 'Shining Hot 20', 'Shining Hot 40', 'Shining Hot 5', 'Cosmic Cash', 'Bomb Bonanza', 'Sugar Rush', 'Koi Pond', 'Rise of Samurai III', 'Big Bass Splash', 'Cash Patrol', 'Queen of Gods', 'Fortune of Giza', 'Zombie Carnival',
    'Wild West Gold Megaways', 'Cleocatra', 'Little Gem', 'The Great Stick-Up', 'Goblin Heist Powernudge', 'Fire Strike 2', 'North Guardians', 'Spirit of Adventure', 'Clover Gold', 'Disco Lady', 'Eye of Cleopatra', 'Chicken Chase', 'Drill that Gold', 'Bull Fiesta', 'Barn Festival', 'Book of Aztec King', 'Spaceman', 'Rainbow Gold', 'Wild Beach Party', 'Queenie', 'Extra Juicy Megaways', 'Snakes and Ladders Megadice', 'Tic Tac Take', 'Might of Ra', 'Elemental Gems Megaways', 
    'The Ultimate 5', 'Colossal Cash Zone', 'Gates of Valhalla', 'Rock Vegas', 'Gold Party', 'Wild Depths', 'Lucky New Year вЂ“ Tiger Treasures', 'MagicianвЂ™s Secrets', 'Hockey Attack', 'Crystal Caverns Megaways', 'Smugglers Cove', 'Christmas Big Bass Bonanza', 'SantaвЂ™s Wonderland', 'Book of Fallen', 'Super X', 'Big Bass Bonanza Megaways', 'Bounty Gold', 'Big Juan', 'John Hunter and the Quest for Bermuda Riches', 'Star Pirates Code', 'Day of Dead', 'Cash Bonanza', 'Mystic Chief', 'Piggy Bank Bills', 'Treasure Wild', 'Starlight Princess', 'Bigger Bass Bonanza', 'Yum Yum Powerways', 'Rise of Giza PowerNudge', 'Fruit Party 2', 'Chicken Drop', 'Book of Vikings', 'Lucky Grace And Charm', 'Empty the Bank', '5 Lions Megaways', 'The Magic Cauldron вЂ“ Enchanted Brew', 'Phoenix Forge', 'Buffalo King Megaways', 'Floating Dragon Hold and Spin', 'Hot Fiesta', 'Power of Thor Megaways', 'Juicy Fruits', 'FishinвЂ™ Reels', 'Temujin Treasures', 'Hot to Burn Hold and Spin', 'Joker King', 'Gates of Olympus', 'The Hand of Midas', 'Eye of the Storm', 'Dragon Kingdom вЂ“ Eyes of Fire', 'Madame Destiny Megaways', 'Congo Cash', 'Emerald King Rainbow Road', 'Golden Ox (Pragmatic Play)', 'Mysterious Egypt', 'Voodoo Magic', 'Big Bass Bonanza', 'John Hunter and the Mayan Gods', 'Spartan King', 'Christmas Carol Megaways', 'Cowboys Gold', 'Dragon Tiger', 'Return of the Dead', 'Emerald King', 'Gems Bonanza', 'Wild Walker', '5 Lions Dance', 'Wild Wild Riches', 'Star Bounty', 'Ultra Hold and Spin', 'Peaky Blinders', 'Curse of the Werewolf Megaways', 'Great Rhino Deluxe', 'Aztec Gems Deluxe', 'Jungle Gorilla', 'The Dog House Megaways', 'Street Racer', 'Drago вЂ“ Jewels of Fortune', 'Pyramid King', 'Starz Megaways', 'Ultra Burn', 'Fruit Party', 'John Hunter and the Book of Tut', 'Great Rhino Megaways', 'Hot to Burn', 'Three Star Fortune', 'Bronco Spirit', 'Fruit Rainbow', 'Wild West Gold', 'The Wild Machine', 'Dance Party', 'Golden Beauty', 'Aztec Bonanza', 'Mysterious', 'Master Joker', 'Super 7s', 'Release the Kraken', 'Magic Journey', 'Buffalo King', 'Greek Gods', 'Money Mouse', 'Sweet Bonanza Xmas', 'Hercules and Pegasus', 'Aladdin and the Sorcerer', 'Honey Honey Honey', 'Fire Strike', 'John Hunter and the Tomb of the Scarab Queen', 'Super Joker', 'Tree of Riches', 'Hot Chilli', 'Vampires vs Wolves', 'The Great Chicken Escape', 'John Hunter and the Aztec Treasure', 'Sweet Bonanza', 'Monkey Warrior', 'Triple Jokers', '5 Lions Gold', 'CaishenвЂ™s Cash', 'Extra Juicy', 'Pirate Gold', 'The Dog House', 'Wild Pixies', 'Safari King', 'Egyptian Fortunes', 'Mustang Gold', 'Treasure Horse', 'Leprechaun Carol', 'Triple Dragons', 'Ancient Egypt Classic', 'Vegas Magic', 'Master ChenвЂ™s Fortune', 'John Hunter Da VinciвЂ™s Treasure', 'Leprechaun Song', 'Peking Luck', 'Jade Butterfly', 'Madame Destiny', 'Asgard', '5 Lions', 'The Champions', 'Great Rhino', 'JokerвЂ™s Jewels', 'Triple Tigers', 'Wild Gladiators', 'Gold Rush', 'Santa', 'PandaвЂ™s Fortuneв„ў', '7 Piggies', 'Diamond Strike', 'Vegas Nights', 'Wild Spells', 'CaishenвЂ™s Gold', 'Pixie Wings', '888 Dragons', 'Jurassic Giants', 'Gold Train', '3 Kingdoms вЂ“ Battle of Red Cliffs', 'Panther Queen', 'Wolf Gold', 'Queen of Gold', 'Diamonds are Forever 3 Lines', 'Hercules Son of Zeus', 'Dragon Kingdom', 'The Catfather Part II', 'Beowulf', 'Mighty Kong', 'Hot Safari', '7 Monkeys', 'Chilli Heat Megaways', 'Book of Kingdoms', 'Pirate Gold Deluxe']
    random_my_list_pragmat = random.choice(my_list_pragmat)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: PragmaticPlay\nСлот: <code>{random_my_list_pragmat}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn2_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_2 = pr_2 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_2 = pr_2 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера PragmaticPlay
@router.callback_query(F.data == 'del2')
async def del2(call: types.CallbackQuery):
    button_number = int('del2'[3:])
    button_number_1 = int('btn2'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: PragmaticPlay',reply_markup=slots)
    await call.message.delete()

#BetSoft
@router.callback_query(F.data == 'btn3')
async def btn3(call: types.CallbackQuery, state: FSMContext):
    my_list_BetSoft = ['Tycoons: Billionaire Bucks', 'Enchanted: Forest of Fortune', 'Triple Lucky 8вЂ™s', 'Rise of Triton', 'Super Golden Dragon Inferno', '72 Fortunes', 'April Fury And The Chamber Of Scarabs', 'Wish Granted', 'Pho Sho Hold & Win', 'Hot Lucky 7s', 'Charms & Treasures', 'Mr. Vegas 2', 'Hearts Desire', 'Expansion!', 'Bounding Luck', 'Woodlanders', 'Golden Dragon Inferno', 'SleighinвЂ™ it', 'Trinity Reels', 'Rags to Witches', 'CaptainвЂ™s Quest Treasure Island', 'Winds of Wealth', 'Wilds of Fortune', 'Book of Helios', 'Gemini Joker', 'Kensei Blades', 'AlkemorвЂ™s Elements', 'Primal Wilderness', 'Lost Mystery Chests', 'Triple Juicy Drops', 'Gold Tiger Ascent', 'Take The Kingdom', 'Stay Frosty!', 'Thai Blossoms', 'Return to Paris', 'Tower of Fortuna', '7 Fortune Frenzy', '88 Frenzy Fortune', 'Wild Drops', 'Lava Gold', 'Safari Sam 2', 'Stacked', 'Take Olympus', 'Golden Horns', 'Take Santas Shop', 'Miles Bellhouse and the Gears of Time', 'Book of Darkness', 'Primal Hunt', 'Dim Sum Prize', 'Mystic Hive', 'The Hive', 'Quest to the West', 'Back to Venus', 'Monster Pop', 'Spring Tails', 'Total Overdrive', 'Super Sweets', 'Dragon & Phoenix', 'Take the Bank', 'CaishenвЂ™s Arrival', 'Gemmed!', 'Bamboo Rush', 'Wolf Moon Rising', 'Gold Canyon', 'Spinfinity Man', 'Viking Voyage', 'Fruit Bat Crazy', 'Fruitbat Crazy', 'Carnaval Forever', 'Faerie Spells', 'Yak Yeti and Roll', 'Chilli Pop', 'Max Quest', 'Dragon Kings', 'The Golden Owl Of Athena', 'Ogre Empire', 'Reels of Wealth', 'Sugarpop 2', 'Legend Of The Nile', 'Blood Eternal', 'GiovanniвЂ™s Gems', 'Fire & Steel', 'The Magic Shoppe', 'The Angler', 'The Slotfather Part 2', 'Fa Fa Twins', 'Kawaii Kitty', 'Fruit Zen', 'Good Girl Bad Girl', 'Sugar Pop', 'Greedy Goblins', 'Lost', 'Madder Scientist']
    random_my_list_BetSoft = random.choice(my_list_BetSoft)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: BetSoft\nСлот: <code>{random_my_list_BetSoft}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn3_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_3 = pr_3 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_3 = pr_3 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера BetSoft
@router.callback_query(F.data == 'del3')
async def del3(call: types.CallbackQuery):
    button_number = int('del3'[3:])
    button_number_1 = int('btn3'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: BetSoft',reply_markup=slots)
    await call.message.delete()

#Red Tiger
@router.callback_query(F.data == 'btn4')
async def btn4(call: types.CallbackQuery, state: FSMContext):
    my_list_RedTiger = ['Vault Cracker Megaways', 'Clover Craze', 'Christmas Morning', 'Giga Blast', 'Steam Squad', 'Sugarlicious EveryWay', 'DragonвЂ™s Mirror', 'Spooky Carnival', 'SirenвЂ™s Riches', 'Hansel and Gretel Candyhouse', 'Year-Round Riches Clusterbuster', 'Easy Gold', 'Case Closed', 'Judgement Day Megaways', 'Sugar Monster', 'Bounty Raid 2', 'Here Kitty Kitty', 'Monsters Unchained', 'London Tube', 'Magic Tricks', 'Desert Legends Spins', 'Cyber Attack', 'Gems Inferno Megaways', 'Astronaut', 'Jelly Multihops', 'Egypt Megaways', 'Alexander the Great: World Conqueror', 'Wolfkin', 'Knights of Avalon', 'Magic Powers Megaways', 'Red Hot BBQ', 'Reel Keeper Power Reels', 'Sheep Gone Wild', 'WrigleyвЂ™s World', 'Cotton Gang Affair', 'Transylvania Night of Blood', 'Happy Apples', 'BugsyвЂ™s Bar', 'Buffalo Mania MegaWays', 'Blobsters Clusterbuster', 'Peggy Sweets', 'Ancient Disco', 'Blood Suckers Megaways', 'Cai Shen 168', 'Pinatas & Ponies', 'Good Luck Clusterbsuter', 'Santa Spins', 'Cake & Ice Cream', 'In The Rabbit Hole', 'Athens MegaWays', 'Shadow Society', 'Stolen Treasures', 'Tricks And Treats', 'Mystery Reels Deluxe', 'Great Gold', 'GonzitaвЂ™s Quest', 'RockвЂ™NвЂ™Lock', 'Bass Boss', 'Gods Of Troy', 'Wanted Wildz', '10 001 Nights MegaWays', 'Majestic Mysteries Power Reels', 'Apache Way', 'Ali BabaвЂ™s Luck Power Reels', 'ZaidaвЂ™s Fortune', 'RisquГ© Megaways', 'Flodder', 'Diamond Royale', 'Big Cat Rescue MegaWays', 'Mayhem', 'Bulls Run Wild', 'Dragons Clusterbuster', 'Cash Or Nothing', 'Viral Spiral', '80s Spins', 'Narcos Mexico', 'Zillard King', 'Genie Nights', 'Doggy Riches Megaways', 'Wild Tundra', 'Last Chance Saloon', 'Fa Fa Babies', 'Get The Gold Infinireels', 'Hustling', 'Blazing Clusters', 'Jingle Ways MegaWays', '1942: Sky Warrior', 'Dracula Awakening', 'Hot Hot Chilli Pot', 'Wild Expedition', 'Hammer Gods', 'Beriched', 'LionвЂ™s Hoard', 'Well of Wilds Megaways', 'Dragon King Legend of the Seas', 'Age Of Akkadia', 'Forever 7s', 'Dynamite Riches Megaways', 'Shah Mat', 'Treasure Mine Power Reels', 'NFT Megaways', 'Amazon Island MegaWays', 'The Wisecracker Lightning', 'Neon Links', 'Tiki Fruits Totem Frenzy', 'Cash Ultimate', 'Cobra Queen', 'Ancients Blessing', 'DragonвЂ™s Luck Deluxe', 'DragonвЂ™s Fire: Infinireels', 'Trillionaire', 'Thors Vengeance', 'Betty, Boris And Boo', 'Regal Beasts', 'Agent Royale', 'War of Gods', 'Regal Streak', 
    'Sylvan Spirits', 'Jingle Bells Power Reels', '10,001 Nights', 'YucatanвЂ™s Mystery', 'Aurum Codex', 'Path of Destiny', 'LeprechaunвЂ™s Magic Megaways', 'Golden Tsar', 'Hoard Of Poseidon', 'Clash Of The Beasts', 'Lucky Fridays', 'Wild OвЂ™Clock', '24 Hour Grand Prix', 'Crystal Mirror', '5 Families', 'Bombuster', 'Ali BabaвЂ™s Luck', 'Cirque DРµ La Fortune', 'GonzoвЂ™s Quest Megaways', 'Gems Gone Wild: Power Reels', 'Captain Rizk Megaways', 'Cash Volt', 'Bounty Raid', 'Reel Keeper', 'Multiplier Riches', 'Aztec Spins', '4Squad', 'Robin HoodвЂ™s Wild Forest', 'Atlantis', 'Zeus Lightning Power Reels', 'The Wild Hatter', 'Vault of Anubis', 'Golden Cryptex', 'Rainbow Jackpots Power Lines', 'LeprechaunвЂ™s Magic', 'Wings of Ra', 'Dice Dice Dice', 'Rio Stars', 'Piggy Riches Megaways', 'Jewel Scarabs', 'Legendary Excalibur', 'Lucky Oktoberfest', 'Eagle Riches', 'Dynamite Riches', 'Jack in a Pot', 'Da VinciвЂ™s Mystery', 'DragonвЂ™s Luck Megaways', 'Mystery Reels Power Reels', 'Wild Elements', 'Fruit Snap', 'Mega Rise', 'DragonвЂ™s Fire MegaWays', 'Well Of Wishes', 'Golden Leprechaun Megaways', 'Royal Gems', 'PiratesвЂ™ Plenty Battle For Gold', 'Mystic Wheel', 'Phoenix Fire Power Reels', 'Wild Cats Multilineв„ў', 'Jester Spins', 'Mega Pyramid', 'Win Escalator', 'Jackpot Quest', 'Five Star Power Reels', 'The Greatest Train Robbery', 'The Equalizer', 'Mega Dragon', 'Reel King Mega', 'Vicky Ventura', 'DevilвЂ™s Number', 'Mystery Reels Megaways', 'Spin Town', 'PiratesвЂ™ Plenty', 'ThorвЂ™s Lightning', 'Gemtastic', 'Ninja Ways', 'Reactor', 'Piggy Pirates', 'Fortune Charm', 'Mayan Gods', 'Totem Lightning Power Reels', 'Flaming Fox', 'DragonвЂ™s Fire', 'Fruit Blox', 'Tiki Fruits', 'Wild Circus', 'Laser Fruit', 'Wild Nords', 'Treasure Mine', 'Rocket Men', 'Masquerade', 'Snow Wild And The 7Features', 'Reel Heist', 'Mystery Reels', 'Lucky Easter', 'Lucky Valentine', 'Imperial Palace', 'Lucky Fortune Cat', 'Stage 888', 'Persian Fortune', 'Five Star', 'Rainbow Jackpots', 'Fortune House', 'Ancient Script', 'Lucky Halloween', 'Golden Temple', 'Wild Wild Chest', 'Gold Star', 'PussвЂ™N Boots', 'Mega Jade', 'DragonвЂ™s Luck', 'Golden Lotus', 'Jade Charms', 'Magic Gate', 'Ocean Fortune', 'Wild Fight', 'Wild Spartans', 'Lucky Wizard', 'Epic Journey', 'Jingle Bells', 'Diamond Blitz']
    random_my_list_RedTiger = random.choice(my_list_RedTiger)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Red Tiger\nСлот: <code>{random_my_list_RedTiger}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn4_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_4 = pr_4 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_4 = pr_4 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Red Tiger
@router.callback_query(F.data == 'del4')
async def del4(call: types.CallbackQuery):
    button_number = int('del4'[3:])
    button_number_1 = int('btn4'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Red Tiger',reply_markup=slots)
    await call.message.delete()

#Big Time Gaming
@router.callback_query(F.data == 'btn5')
async def btn5(call: types.CallbackQuery, state: FSMContext):
    my_list_BigTimeGaming = ['Bonanza Falls', 'Christmas Catch', 'Sanctuary', 'More Turkey Megaways', 'Wild Unicorns', 'Max Megaways 2', 'Big Bad Bison Megaways', 'Vegas Rush', 'Over the Moon', 'The Race Megaways', 'Gifts of Fortune Megaways', 'Rasputin Megaways', 
    'Christmas Bonanza', 'Outlaw', 'Castle of Terror', 'Max Megaways', 'Danger High Voltage Megapays', 'Vegas Megaways', 'Millionaire Rush', 'Wild Portals Megaways', 'Golden Catch', 'Star Clusters Megapays', 'Apollo Pays Megaways', 'Diamond Fruits', 'Pirate Pays Megaways', 'Kingmaker Fully Loaded Megaways', 'Slot Vegas Fully Loaded', 'Who Wants To Be A Millionaire Megapays', 'Gold Megaways', 'Spicy Meatballs Megaways', 'Pop', 'Wheel of Fortune Megaways', 'Cyberslot Megaclusters', 'Chocolates', 'Slot Vegas Megaquads', 'Star Clusters Megaclusters', 'Survivor Megaways', 'Royal Mint', 'Monopoly Megaways', 'Who Wants to Be a Millionaire Mystery Box', 'Lil Devil', 'Kingmaker', 'Opal Fruits', 'The Final Countdown', 'Holy Diver', 'Who Wants To Be A Millionaire Megaways', 'Donuts', 'Book of Gods', 'Extra Chilli', 'Temple Quest Spinfinity', 'White Rabbit', 'Danger High Voltage', 'Bonanza', 'StarQuest', 'Queen of Riches', 'Dragon Born']
    random_my_list_BigTimeGaming = random.choice(my_list_BigTimeGaming)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Big Time Gaming\nСлот: <code>{random_my_list_BigTimeGaming}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn5_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_5 = pr_5 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_5 = pr_5 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Big Time Gaming
@router.callback_query(F.data == 'del5')
async def del5(call: types.CallbackQuery):
    button_number = int('del5'[3:])
    button_number_1 = int('btn5'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Big Time Gaming',reply_markup=slots)
    await call.message.delete()

#Relax Gaming
@router.callback_query(F.data == 'btn6')
async def btn6(call: types.CallbackQuery, state: FSMContext):
    my_list_RelaxGaming = ['Bill & Coin', 'The Sorcerers Shuffle Dream Drop', 'Los Cuatro Esqueletos Dream Drop', 'Galactic Racers', 'Swag Bag Bonanza', 'TeslaвЂ™s Invention', 'Lure of Fortune', 'The Sorcerers Shuffle', 'SnakeвЂ™s Gold Dream Drop', 'Titan Strike', 'Money Train 4', 'Jungle Jamboree Dream Drop', 'Dead ManвЂ™s Trail Dream Drop', 'Joker Split', 'PiГ±ata Popper Dream Drop', 'Phoenix Up Cash', 'Torii Tumble', 'Los Cuatro Esqueletos', 'Castaway Cove', 'Midnight Marauder Dream Drop', 'Sloth Tumble', 'Shark Wash', 'Cluster Tumble Dream Drop', 'Money Train Origins Dream Drop', 'Otterly Amazing', 'Towering Ways Aztec', 'Fly Cats Dream Drop', '5 Monsters', 'Hypernova Infinity Reels Dream Drop', 'Mega Heist', 'Hellcatraz 2 Dream Drop', 'Money Cart 3', 'Banana Town Dream Drop', 'Beellionaires Dream Drop', 'Book of Power', 'Wild Chapo 2', 'Wild Hike', 'Pine of Plinko Dream Drop', 'Horror Hotel', 'Grim The Splitter Dream Drop', 'Net Gains', 'Reel Star', 'Tiki Bonanza', 'SantaвЂ™s Stack Dream Drop', 'Wild Yield', 'Dueling Jokers Dream Drop', 'Hot Rod Racers', 'Templar Tumble 2 Dream Drop', 'Spring Heeled Jack', 'The Great Pigsby Megaways', 'Dream Drop Diamonds', 'Wild Donuts', 'Golden Calaveras', 'Money Train 3', 'Neko Night Dream Drop', 'Dead Riders Trail', 'Lucky Money', 'Shamrock Money Pot 10K ways', 'TNT Tumble Dream Drop', 'Wild Chapo Dream Drop', '4 Secret Pyramids', 'Volatile Vikings 2 Dream Drop', 'Checkmate Hot1', 'Banana Town', 'Flower Fortunes Supreme', 'Blender Blitz', 'Curse of the Mummies', 'Snake Arena Dream Drop', 'Midnight Marauder', 'Out of the Ice', 'Alchemy', 'Temple Tumble 2', 'Magikspell', 'Jurassic Party', '7 Elements', 'Super Massive Infinity Reels', 'The Great Pigsby Megapays', 'Alice In Adventureland', 'Bounty 98 Hot 1', 'Payday Megaways', 'Templar Tumble', 'Hex', 'Clover Fortunes', 'The TrollsвЂ™ Treasure', 'Tiger Kingdom Infinity Reels', 'Beast Mode', 'Jungle Jamboree', 'Space Miners', 'Star Pop', 'Hazakura Ways', 'Plunderland', 'Money Cart Bonus Reels', 'Royal Potato', 'SantaвЂ™s Stack', 'Cluster Tumble', 'Mega Mine', 'Crystal Golem', 'Helios Furya', 'Volatile Vikings', 'Hypernova Infinity Reels', 'Dead Mans Trail', 'Temple Frenzy Lightning Chase', 'TrollвЂ™s Gold', 'Deep Descent', 'Money Cart 2', 'Top Dawg$', '3 Secret Cities', 'Book of 99', 'Golden Castle', 'Elemento', 'The Golden Sail', 'Multiplier Odyssey', 'Kluster Krystals Megaclusters', 'Maze Escape Megaways', 'Christmas Santa', 'Sherlock Bones', '123 Boom!', 'Iron Bank', 'Ramses Revenge', 'Twisted Turbine', 'Super Boost', 'Money Train 2', '6 Wild Sharks', 'La Fiesta', 'Serpent Shrine', 'Odin Infinity Reels Megaways', 'Marching Legions', 'Mega Flip', 'Yummy Wilds', 'Hellcatraz', 'Heroes Hunt Megaways', 'TNT Tumble', 'Blazing Bull', 'Aurora', 'Mega Masks', 'Desert Shark', 'Sugar Cubes', 'Heroes Gathering', 'Snake Arena', 'Trail Blazer', 'Big Bounty Bill', 'Tower Tumble', 'ItвЂ™s Time', 'LetвЂ™s Get Ready To Rumble', 'Money Train', 'Ignite The Night', 'Wildchemy', 'Temple Tumble', 'Machina', 'Electric Wilds']
    random_my_list_RelaxGaming = random.choice(my_list_RelaxGaming)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Relax Gaming\nСлот: <code>{random_my_list_RelaxGaming}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn6_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_6 = pr_6 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_6 = pr_6 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Relax Gaming
@router.callback_query(F.data == 'del6')
async def del6(call: types.CallbackQuery):
    button_number = int('del6'[3:])
    button_number_1 = int('btn6'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Relax Gaming',reply_markup=slots)
    await call.message.delete()

#Play'n GO
@router.callback_query(F.data == 'btn7')
async def btn7(call: types.CallbackQuery, state: FSMContext):
    my_list_PlayGO = ['Pandastic Adventure', 'Viking Runecraft 100', 'Mega Don Feeding Frenzy', 'Gargantoonz', 'Invading Vegas: Las Christmas', 'Legacy of Dynasties', 'Sherwood Gold', 'Monkey: Battle for the Scrolls', 'Ruff Heist', 'Raging Rex 3', 'Return of the Green Knight', 'Piggy Blitz', 'Temple of Prosperity', 'Scales of Dead', 'Boat Bonanza Colossal Catch', 'Honey Rush 100', 'Hugo Legacy', 'Sweet Alchemy 100', 'Scroll of Seth', 'Merlin: Journey of Flame', 'Fox Mayhem', 'Sparky and Shortz Hidden Joules', 'Rascal Riches', 'Sweet Alchemy 2', 'Ternion', 'Viking Runecraft: Apocalypse', 'Free Reelin Joker 1000', 'Highway Legends', 'Luchamigos', 'Captain Glum: Pirate Hunter', 'Gerard’s Gambit', 'Ronin’s Honour', 'Slashimi', 'Craps', 'Wild Bandolier', 'Moon Princess Trinity', 'Pandora’s Box of Evil', 'Colt Lightning', 'Legion Gold', 'Legacy of Inca', 'Game of Gladiators Uprising', 'Pilgrim of Dead', 'Invading Vegas', 'Cash-a-Cabana', 'Shamrock Miner', 'Mötley Crüe', 'Wild Falls 2', 'Naughty Nick’s Book', 'Athena Ascending', 'Clash of Camelot', 'USA Flip', 'Rise of Olympus 100', 'Canine Carnage', 'Count Jokula', 'Boat Bonanza', 'Dio — Killing the Dragon', 'Fortune Rewind', 'ImmorTails of Egypt', 'Gates of Troy', 'Mount M', 'Champions of Mithrune', 'Bull in a Rodeo', 'Forge of Fortunes', 'Leprechaun’s Vault', 'Dutch Flip', 'Mega Don', 'Cash of Command', 'Rotiki', 'Merlins Grimoire', 'NSYNC Pop', 'Cat Wilde and the Pyramids of Dead', 'Rocco Gallo', 'Derby Wheel', 'Wild Trigger', 'King’s Mask', 'Animal Madness', 'Idol of Fortune', 'Rise of Gods Reckoning', 'Lordi Reel Monsters', 'Puebla Parade', 'Forge of Gems', 'Def Leppard Hysteria', 'Eye of Atum', 'Raging Rex 2', 'Fat Frankies', 'Safari of Wealth', 'Secret of Dead', 'Tales of Asgard Freya’s Wedding', 'Cat Wilde and the Lost Chapter', 'Gigantoonz', 'Love Joker', '15 Crystal Roses A Tale of Love', 'Tale of Kuybiko', 'Captain Xenos Earth Adventure', 'Beasts of Fire', 'Moon Princess 100', 'Hooligan Hustle', 'KISS Reels of Rock', 'Moon Princess Christmas Kingdom', 'Merlin and the Ice Queen Morgana', 'Rich Wilde and the Wandering City', 'The Last Sundown', 'Legend of the Ice Dragon', 'Tales of Asgard: Loki’s Fortune', 'Snakebite', 'Muerto En Mictlan', 'Sparky and Shortz', 'Alice Cooper and the Tome of Madness', 'Charlie Chance and the Curse of Cleopatra', 'The Wild Class', 'Ghost of Dead', 'Dr Toonz', 'Sisters of the Sun', 'Hugo Carts', 'Agent of Hearts', 'Diamonds of the Realm', 'ZZ Top Roadside Riches', 'Odin Protector of Realms', 'Hotel Yeti-Way', 'Gemix 2', 'Scroll of Dead', 'Court of Hearts', 'Fire Joker Freeze', 'Fire Toad', 'Rich Wilde And The Amulet of Dead', 'Shimmering Woods', 'House of Doom 2: The Crypt', 'The Green Knight', 'The Faces of Freya', 'The Paying Piano Club', 'Thunder Screech', 'Cat Wilde in the Eclipse of the Sun God', 'Lord Merlin and the Lady of the Lake', 'Bull in a China Shop', 'Miner Donkey Trouble', 'Coils of Cash', 'Piggy Bank Farm', 'Golden Osiris', 'Frozen Gems', 'Ice Joker', 'New Year Riches', '24K Dragon', 'Rise of Athena', 'Holiday Spirits', 'Disco Diamonds', 'Madame Ink', 'Helloween', 'Rabbit Hole Riches', 'Reactoonz 2', 'Feline Fury', 'Beast of Wealth', 'Celebration of Wealth', 'Temple of Wealth', 'Octopus Treasure', 'Golden Ticket 2', 'Jolly Roger 2', 'Diamond Vortex', 'Saxon', 'Blinged', 'Riddle Reels: A Case of Riches', 'Win A Beest', 'Gold Volcano', 'Nyjah Huston — Skate for Gold', 'Cat Wilde and the Doom of Dead', 'Troll Hunters 2', 'Rally 4 Riches', 'Twisted Sister', 'Rich Wilde and the Shield of Athena', 'Charlie Chance: In Hell To Pay', 'Agent Destiny', 'Annihilator', 'Ring of Odin', 'That’s Rich', 'Sticky Joker', 'Riches of Robin', 'Testament', 'Fortunes of Alibaba', 'Dawn of Egypt', 'Leprechaun Goes Wild', 'Coywolf Cash', 'Wild Blood 2', 'Wildhound Derby', 'Legacy of Dead', 'Wild Frames', 'Divine Showdown', 'Ankh of Anubis', 'Chronos Joker', 'Xmas Magic', 'Black Mamba', 'Doom of Egypt', 'Honey Rush', 'Big Win 777', 'Cash Pump', 'Rainforest Magic', 'Demon', 'Mission Cash', 'Inferno Joker', 'Hugo’s Adventure', 'Rise of Dead', 'The Sword and The Grail', 'Firefly Frenzy', 'Wild Rails', 'Tome of Madness', 'Rise of Merlin', 'Sabaton', 'Game of Gladiators', 'Perfect Gems', 'Inferno Star', 'Mahjong 88', 'Crystal Sun', 'Phoenix Reborn', 'Cash Vandal', 'Contact', 'Golden Colts', 'Queen’s Day Tilt', 'Wild Falls', 'Raging Rex', 'Star Joker', 'Battle Royal', 'Banana Rock', 'Dragon Maiden', 'Gunslinger Reloaded', 'Cloud Quest', 'Golden Caravan', 'Holiday Season', 'Hugo', 'Hugo Goal', 'Iron Girl', 'Rise Of Olympus', 'Samba Carnival', 'Sizzling Spins', 'Street Magic', 'Cops ‘n’ Robbers', 'Legacy of Egypt', 'Sweet Alchemy', 'Planet Fortune', 'Mystery Joker 6000', 'Sea Hunter', 'Hugo 2', 'Big Win Cat', 'Fu Er Dai', 'Reactoonz', 'Mermaid’s Diamond', 'Moon Princess', 'Viking Runecraft', '7 Sins', 'Grim Muerto', 'Fire Joker', 'Rich Wilde and the Book of Dead', 'Xmas Joker', 'Royal Masquerade', 'Eye of The Kraken', 'Wild North', 'Spin Party', 'Super Flip', 'Golden Legend', 'Tower Quest', 'Pimped', 'Gemix', 'Merry Xmas', 'Golden Ticket', 'Pearls Of India', 'Mystery Joker', 'Lady of Fortune', 'Energoonz', 'Rage To Riches', 'Troll Hunters', 'Ninja Fruits', 'Cats and Cash', 
    'Jolly Roger', 'Space Race']
    random_my_list_PlayGO = random.choice(my_list_PlayGO)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Play`n GO\nСлот: <code>{random_my_list_PlayGO}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn7_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_7 = pr_7 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_7 = pr_7 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Play'n GO
@router.callback_query(F.data == 'del7')
async def del7(call: types.CallbackQuery):
    button_number = int('del7'[3:])
    button_number_1 = int('btn7'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Play`n GO',reply_markup=slots)
    await call.message.delete()

#Playson
@router.callback_query(F.data == 'btn8')
async def btn8(call: types.CallbackQuery, state: FSMContext):
    my_list_Playson = ['Crystal Land 2', 'Jelly Valley', 'Fire Temple: Hold and Win', 'Sherwood Coins: Hold and Win', 'Diamonds Power: Hold and Win', 'Fire Coins: Hold and Win', 'Pearl Ocean: Hold and Win', '777 Sizzling Wins: 5 Lines', 'Energy Coins: Hold and Win', 'Crown & Diamonds: Hold and Win', 'Wolf Land: Hold and Win', '3 Pots Riches: Hold and Win', 'Empire Gold: Hold and Win', 'Royal Fortunator: Hold and Win', 'Buffalo Power 2: Hold and Win', 'Coin Strike: Hold and Win', 'Giza Nights: Hold and Win', 'Royal Joker: Hold and Win', 'Bozo Cats', 'Mammoth Peak: Hold and Win', 'Pirate Chest: Hold and Win', 'Hit the Bank Hold and Win', 'Treasures of Fire: Scatter Pays', 'Pirate Sharky', 'Royal Coins 2: Hold and Win', 'Ultra Fortunator: Hold and Win', 'Ruby Hit: Hold and Win', 'Luxor Gold: Hold and Win', 'Juice Inc.', 'Book del Sol: Multiplier', 'Lion Gems: Hold and Win', 'Burning Fortunator', 'Wolf Power Megaways', 'Joker’s Coins: Hold and Win', 'Diamond Fortunator: Hold and Win', 'Buffalo Power Christmas', 'Solar Queen Megaways', 'Burning Wins x2', 'The Fruit Megaways', 'Royal Coins Hold and Win', 'Spirit of Egypt: Hold and Win', 'Eagle Power: Hold and Win', '5 Fortunator', 'Hot Burning Wins', '9 Happy Pharaohs', 'Buffalo Power: Megaways', 'Rich Diamonds: Hold and Win', 'Hot Coins: Hold and Win', 'Wolf Power: Hold and Win', '5 Super Sevens & Fruits', 'Super Sunny Fruits', 'Solar King', 'Book of Gold Multichance', 'Diamond Wins: Hold & Win', 'Buffalo Power', 'Solar Temple', 'Sunny Fruits: Hold and Win', 'Legend of Cleopatra Megaways', 'Red Chilli Wins', 'Book of Gold: Symbol Choice', 'Clover Riches', 'Imperial Fruits: 100 lines', 'Solar Queen', 'Imperial Fruits: 40 lines', 'Book of Gold: Classic', '3 Fruits Win: 10 lines', 'Fruits & Jokers: 100 Lines', 'Sakura Dragon', 'Vikings Fortune: Hold and Win', 'Imperial Fruits: 5 lines', 'Sevens&Fruits: 20 Lines', 'Fruits & Clovers 20 lines', 'Mighty Africa', '100 Joker Staxx', 'Crystal Crush', 'Lucky Staxx 40 lines', 'Wild Warriors', 'Fruits and Jokers: 40 lines', 'Fruits & Joker', 'Book of Gold: Double Chance', 'Joker Expand: 40 lines', 'Chicago Gangsters', 'Phoenix Fire', 'Fruits & Jokers: 20 lines', 'Super Burning Wins: classic 5 lines', 'Rise of Egypt', 'Joker Expand: 5 lines', 'God of Wild Sea', 'Burning Wins: classic 5 lines', 'Sevens & Fruits', 'Kingdom of the Sun – Golden Age', 'Legend of Cleopatra', 'Fruits’N’Stars: Holiday Edition', 'Crystal Land', 'Viking Gods: Thor and Loki', 'Fireworks Master', 'Treasures of Tombs Hidden Gold', 'Burlesque Queen']
    random_my_list_Playson = random.choice(my_list_Playson)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Playson\nСлот: <code>{random_my_list_Playson}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn8_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_8 = pr_8 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_8 = pr_8 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Playson
@router.callback_query(F.data == 'del8')
async def del8(call: types.CallbackQuery):
    button_number = int('del8'[3:])
    button_number_1 = int('btn8'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Playson',reply_markup=slots)
    await call.message.delete()

#Wazdan
@router.callback_query(F.data == 'btn9')
async def btn9(call: types.CallbackQuery, state: FSMContext):
    my_list_Wazdan = ['Hot Slot™: 777 Stars Extremely Light', '9 Bells™', '20 Coins™', 'Book of Faith™', 'Black Horse™ Cash Out Edition', '12 Coins™ Grand Gold Edition', 'Hot Slot™: 777 Coins Extremely Light', 'Mighty Symbols™: Diamonds', 'Sizzling Eggs™ Extremely Light', 'Los Muertos™ II', '9 Coins™ Grand Diamond Edition', 'Hot Slot™: 777 Cash Out Extremely Light', 'Burning Sun™ Extremely Light', '9 Coins™ Extremely Light', 'Mighty Symbols™: Crowns', '16 Coins™', '9 Coins™ Grand Platinum Edition', 'Mighty Wild™: Panther', 'Moon of Fortune', '15 Coins™', '12 Coins™', 'Hot Slot™: 777 Coins', 'Hot Slot™: 777 Cash Out', 'Mystery Kingdom™: Mystery Bells', 'Hot Slot™: Great Book of Magic', 'Hot Slot™: 777 Rubies', 'Hot Slot™: 777 Stars', 'Power of Sun™: Svarog', 'Hot Slot™: Mystery Jackpot Joker', '9 Coins™ Grand Gold Edition', 'Burning Sun™', 'Hot Slot™: Magic Pearls', 'Hot Slot™: Magic Bombs', '9 Coins™: 1000 Edition', '9 Burning Stars™', 'Sizzling Kingdom™: Bison', 'Power of Gods: Valhalla', '9 Coins™', 'Sizzling Eggs™', '9 Burning Dragons', 'Magic Spins', 'Hot Slot™: 777 Crown', 'Magic Eggs', 'Dwarfs Fortune™', 'Sizzling Moon™', 'Power of Gods: Medusa', 'Jelly Reels™', 'Sizzling Bells™', 
    'Power of Gods: Hades', 'Fortune Reels', 'Midnight in Tokyo', 'Prosperity Pearls', 'Sun of Fortune', 'Burning Stars 3™', 'Clover Lady™', 'Unicorn Reels', 'Reel Joke™', '9 Lions', 'Magic Fruits', 'Magic Fruits Deluxe', 'Magic Target Deluxe', 'Lucky Queen', 'Beach Party', 'Lost Treasure (Wazdan)']
    random_my_list_Wazdan = random.choice(my_list_Wazdan)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Wazdan\nСлот: <code>{random_my_list_Wazdan}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn9_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_9 = pr_9 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_9 = pr_9 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Wazdan
@router.callback_query(F.data == 'del9')
async def del9(call: types.CallbackQuery):
    button_number = int('del9'[3:])
    button_number_1 = int('btn9'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Wazdan',reply_markup=slots)
    await call.message.delete()

#Amatic
@router.callback_query(F.data == 'btn10')
async def btn10(call: types.CallbackQuery, state: FSMContext):
    my_list_Amatic = ['Mr. Magic', 'Book of Montezuma', 'Cash Diamonds', 'Cash & Crab', 'Relic Riches', 'Hot Seven Deluxe', 'All Ways Hottest Fruits', 'Double Diamonds', 'Chilli Willie', 'Lucky Shark', 'Wild Boost', 'Diamond Staxx', 'Lucky Joker Xmas', 'Hot Football', 'Burning Bells 10', 'All Ways Candy', 'Wild Witches', 'Wild Shark Bonus Buy', 'Hot Scatter Deluxe', 'Fruit Star', 'Lucky Golden 7', 'Lucky Joker 10 Cash Spins', 'Bounty Bonanza', 'Book of Admiral', 'Billyonaire Bonus Buy', 'Lady Fruits 100 Easter', 'Joker X', 'Wild Anubis', 'Sun Goddess', 'Hot Fruits 20 Cash Spins', 'Grand Wild Dragon 20', 'Burning Bells 20', 'Santas Fruits', 'Wild Hearts', 'Fruit Loop', 'Aztec Emerald', 'Pharaohs Gold 20', 'Allways Hot Fruits', 'Lucky Double', 'Hot Fruits 10', 'Wild Volcano', 'Hot Soccer', 'Allways Fruits', 'Book of Fruits 10', 'Princess of Pearls', 'Fiery Fruits', 'Lucky Joker 10', 'Buffalo Thunderstacks', 'Lady Fruits 40 Easter', 'Book Of Fruits 20', 'Tiki Madness 100', 'Lovely Lady Deluxe', 'Fruit Express', 'Triple Wild', 'Casanovas Ladies', 'Nicer Dice 100', 'Book of Aztec Select', 'Lady Fruits 20', 'Book of Aztec Bonus Buy', 'Lovely Lady X-Mas', 'Nicer Dice 40', 'Mega Shark', 'Book of Fruits Halloween', 'Oktoberfest', 'Lucky Joker 100', 'Dragons Mystery', 'Harlequeen', 'Hot Choice Deluxe', 'Lucky Respin', 'Crazy Bee', 'Plenty Dragons', 'Hot Fruits 27', 'Book of Fruits', 'Hot Fruits Deluxe', 'Chinese Spider', 'Fortune Girl', 'Fruit Box', 'Golden Quest', 'Grand Fruits', 'Fire Queen', 'Grand Casanova', 'Dia Muertos', 'Hottest Fruits 20', 'Book Of Pharao', 'Hottest Fruits 40', 'Hot Fruits 40', 'Lucky Joker 40', 'Super Cats', 'Beauty Warrior', 'Book of Lords', 'Book of Queen', 'Party Night', 'Lucky Joker 20', 'Dragon’s Gift', 'Hot fruits 100', 'King of Dwarves', 'Golden Joker', 'Sakura Fruits', 'Lightning Hot', 'Hot 40', 'Lucky Little Devil', 'Beauty Fairy', 'Hot Fruits 20', 'Flying Dutchman', 'Enchanted Cleopatra', 'All Ways Joker', 'Lucky Zodiac', 'Big Panda', 'King’s Crown', 'Hot Neon', 'Mermaid’s Gold', 'Ultra Seven', 'All Ways Win', 'La Gran Aventura', 'Casanova', 'Billyonaire', 'Gem Star', 'Diamond Monkey', 'Red Chilli', 'Cool Diamonds 2', 'Scarab Treasure', 'Hot Diamonds', 'Bells on Fire Hot', 'Hot 27', 'Hot 81', 'Fire & Ice', 'Golden Book', 'Crystal Fruits', 'Lucky Joker 5', 'Eye of Ra', 'Dragons Kingdom', 'Grand Tiger', 'Hot Choice', 'Vampires', 'Diamonds on Fire', 'Bells on Fire Rombo', 'Hot Seven', 'Lucky Bells', 'Arising Phoenix', 'Hot Twenty', 'Lady Joker', 'Lovely Lady', 'Lucky Coin', 'Royal Unicorn', 'Book of Aztec', 'Wild Dragon', 'Wolf Moon', 'Grand X', 'Wild Stars', 'Book of Fortune', 'Casinova', 'Merry Fruits', 'Blue Dolphin', 'Party Time', 'Admiral Nelson', 'Billy’s Game', 'Magic Owl', 'Wild 7', 'Magic Idol', 'Magic Forest', 'Bells on Fire', 'Dragons Pearl', 'Wild Shark', 'Aztec Secret', 'Tweety Birds', 'Wild Respin', 'Hot Scatter', 'Hot Star', 'Diamond Cats', 'Fortunas Fruits']
    random_my_list_Amatic = random.choice(my_list_Amatic)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Amatic\nСлот: <code>{random_my_list_Amatic}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn10_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_10 = pr_10 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_10 = pr_10 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Amatic
@router.callback_query(F.data == 'del10')
async def del10(call: types.CallbackQuery):
    button_number = int('del10'[3:])
    button_number_1 = int('btn10'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Amatic',reply_markup=slots)
    await call.message.delete()

#Yggdrasil 
@router.callback_query(F.data == 'btn11')
async def btn11(call: types.CallbackQuery, state: FSMContext):
    my_list_Yggdrasil = ['Legend of the Dragon Wins DoubleMax', 'Rock Star Santa MultiMax', 'Diggin’ For Diamonds', 'Excalibur VS Gigablox', 'Mega Money Machine', 'Juiced DuoMax', 'Defenders of Mystica', 'Wild Stack Frenzy', 'Vampire Riches DoubleMax', 'Fatz’s Diner', 'Lotus Warrior', 'Blackbeard Battle Of The Seas', 'Hercules 10k Ways', 'GigaGong GigaBlox', 'Enchanted Waters', 'Roamin Romans Ultranudge', 'Shaker Club', 'Nightmares VS GigaBlox', 'Notre-Dame Tales GigaBlox', 'Fast Fruits Doublemax', 'Bucks And Doe 10K Ways', 'Mayan Waterfalls', 'Badger Miners', 'Starfire Fortunes TopHit', 'Beasty Blox Gigablox', 'Jokrz Wild Ultranudge Gigablox', 'Candyfinity', 'Orca’s Wild Bonanza', 'RagnaWolves WildEnergy', '10 Hot Hotfire', 
    'Purrfect Potions', 'Devour The Weak', 'Giganimals Gigablox', 'Nice Catch DoubleMax', 'Gold Fever', 'E-Force', 'Big Bucks Buffalo Gigablox', 'Bugs Money', 'Winterberries 2', 'Fury of Hyde Megaways', 'Elysian Jackpots', 'Power of Love', 'Neon Villains', 'Fu 10K Ways', 'Dragonblox Gigablox', 'The Legend of Musashi', 'Rainbow Power Pots', 'Gods vs Gigablox', 'Christmas Plaza DoubleMax', 'Cannonade!', 'Desperate Dawgs 2 Gigablox', 'Firekick! Multimax', 'Dragon Lore Gigarise', 'Florageddon!', 'Jekyllz Wild Ultranudge', 'Champion of the Underworld', 'Calavera Crush', 'Wild Fishin Wild Ways', 'Hillbilly Vegas', 'Of Sabers and Monsters', 'Midway Money', 'Prized Pets Gigablox', 'Book HOTFIRE', 'Monsters vs Gigablox', 'MexoMax!', 'Dublin Up Doublemax', 'Professor Clank’s Combinator', 'Mega Cash Stack', 'Wild 1', 'Buffalo Blox Gigablox', 'Tempered Steel', 'Eye of Persia 2', '4 Fantastic Fish', 'Big Benji Bonanza', 'Boilin’ Pots', 'Jokrz Wild Ultranudge', 'LolliPop', 'Achilles', 'Vikings Go To Valhalla', '60 Second Heist', 'Pushy Cats', 'Super Cash Drop Gigablox', 'Time Machine', 'Tiki Runner 2 DoubleMax', 'Dead Mans Fingers', 'Cazino Zeppelin Reloaded', 'Steam Spin', 'Cthulhu', 'Age of Beasts Infinity Reels', 'Valhalla Saga Thunder of Thor', 'Gator Gold Deluxe', 'Glory of Heroes', '90K Yeti Gigablox', 'Golden Fish Tank 2 Gigablox', 'Serendipity', 'Savanna Roar', 'Tiger Tiger: Wild Life', 'Hunters Moon Gigablox', 'Vikings Go Berzerk Reloaded', 'Medusa Hot 1', 'Hammer of Gods', 'PiggyPop', 'Swords and Sabres: Charge Gigablox', 'PapayaPop', 'Raptor Doublemax', '3021 The Bounty Hunter Gigablox', 'Victoria Wild Deluxe', 'Siren Song', 'Golden Gorgon', 'Super Cash Drop', 'Crystal Falls Multimax', 'Tiki Infinity Reels Megaways', 'Robin – Nottingham Raiders', '12 Trojan Mysteriesa', 'Suncatcher Gigablox', 'Krazy Klimber', 'Lady Merlin Lightning Chase', 'The Mafiosi', 'Atlantean Gigarise', 'Robin — Sherwood Marauders', 'Johnan Legendarian', 'Easter Island 2', 'Zombies At The Door', 'Buster Hammer Carnival', 'Thor Infinity Reels', 'Desperate Dawgs', 'Labyrinth of Knossos Multijump', 'TikiPop', 'Reel Desire', 'Ancient Eclipse', 'Frost Queen Jackpots', 'Christmas Tree', 'Pirates 2 Mutiny', 'Atlantis Megaways', 'BountyPop', 'Carol of the Elves', 'Syncronite Splitz', 'Moley Moolah', 'Elemental Princess', 'Hades Gigablox', 'Hyperburst', 'Rock the Cash Bar', 'CherryPop', 'Victoria Wild', 'Valley of the Gods 2', '2 Gods Zeus vs Thor', 'Jackpot Express', 'Football Glory', 'Medusa — Fortune and Glory', 'Vault of Fortune', 'Big Bucks Bandits Megaways', 'Wild Pops', 'All Star Knockout Ultra Gamble', 'Lucky Neko Gigablox', 'Avatars: Gateway Guardians', 'Lightning Joker', 'Blood Moon Wilds', 'Arthur’s Fortune', 'El Dorado Infinity Reels', 'Giza Infinity Reels', 'Neon Rush Splitz', 'Wilhelm Tell', 'Multifly', 'Pirates Smugglers Paradise', 'All Star Knockout', 'PopRocks', 'The Royal Family', 'Brazil Bomba', 'Time Travel Tigers', 'Ice and Fire', 'Temple Stacks', 'Aldo’s Journey', '9k Yeti', 'Santa 9K Yeti', 'Age of Asgard', 'Lilith’s Inferno', 'Sahara Nights', 'Nikola Tesla’s Incredible Machine', 'Yokozuna Clash', 'The One Armed Bandit', 'Wild Robo Factory', 'Jackpot Raiders', 'Niagara Falls', 'Dr Fortuno', 'Dwarf Mine', 'Champions of Rome', 'Cazino Cosmos', 'Trolls Bridge', 'Baron Samedi', 'Nitro Circus', 'Dark Vortex', 'Wolf Hunters', 'Hanzo’s Dojo', 'Penguin City', 'Tut’s Twister', 'Vikings Go To Hell', 'Fruitoids', 'Lucha Maniacs', 'Easter Island', 'Gem Rocks', 'Ozwin’s Jackpots', 'Orient Express', 'Reptoids', 'Pumpkin Smash', 'Jungle Books', 'Valley Of The Gods', 'Rainbow Ryan', 'Spina Colada', 'Sunny Shores', 'Power Plant', 'Chibeasties 2', 'Beauty and the Beast (Yggdrasil)', 'Alchymedes', 'Vikings Go Berzerk', 'Nirvana', 'Super Heroes', 'Empire Fortune', 'Wicked Circus', 'Double Dragons', 'Big Blox', 'Legend of the White Snake Lady', 'Bicicleta', 'Legend of the Golden Monkey', 'Jokerizer', 'Seasons', 'Golden Fish Tank', 'Winterberries', 'Incinerator', 'Cazino Zeppelin', 'Doubles', 'Holmes & the Stolen Stones', 'Vikings Go Wild', 'Chibeasties', 'Cyrus the Virus', 'Joker Millions', 'The Dark Joker Rizes', 'Reef Run']
    random_my_list_Yggdrasil = random.choice(my_list_Yggdrasil)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Yggdrasil\nСлот: <code>{random_my_list_Yggdrasil}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn11_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_11 = pr_11 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_11 = pr_11 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Yggdrasil
@router.callback_query(F.data == 'del11')
async def del11(call: types.CallbackQuery):
    button_number = int('del11'[3:])
    button_number_1 = int('btn11'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Yggdrasil',reply_markup=slots)
    await call.message.delete()

#NolimitCity
@router.callback_query(F.data == 'btn12')
async def btn12(call: types.CallbackQuery, state: FSMContext):
    my_list_NolimitCity = ['Devil’s Crossroad', 'Jingle Balls', 'Nine To Five', 'Roadkill', 'Ugliest Catch', 'Space Donkey', 'The Crypt', 'DJ Psycho', 'True Kult', 'Bounty Hunters', 'The Cage', 'Gluttony', 'Whacked!', 'Disturbed', 'Kiss My Chainsaw', 'Blood & Shadow', 'Benji Killed In Vegas', 'Walk of Shame', 'Dead Canary', 'Pearl Harbor', 'Rock Bottom', 'Serial', 'Little Bighorn', 'The Border', 'Road Rage', 'The Rave', 'Folsom Prison', 'Karen Maneater', 'Remember Gulag', 'Misery Mining', 'Punk Toilet', 'Tombstone RIP', 'True Grit Redemption', 'Legion X', 'Evil Goblins', 'Das xBoot', 'Mental', 'xWays Hoarder xSplit', 'Infectious 5', 'Bushido Ways', 'Fire in the Hole', 'East Coast vs West Coast', 'San Quentin xWays', 'Tomb of Akhenaten', 'Warrior Graveyard', 'Monkey’s Gold xPays', 'Buffalo Hunter', 'Book of Shadows', 'Immortal Fruits', 'Milky Ways', 'Golden Genie', 'Bonus Bunnies', 'Deadwood xNudge', 'Harlequin Carnival', 'Barbarian Fury', 'Punk Rocker', 'Poison Eve', 'Dragon Tribe', 'Tomb Of Nefertiti', 'Pixies Vs Pirates', 'Tractor Beam', 'Tombstone', 'Ice Ice Yeti', 'Space Arcade']
    random_my_list_NolimitCity = random.choice(my_list_NolimitCity)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: NolimitCity\nСлот: <code>{random_my_list_NolimitCity}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn12_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_12 = pr_12 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_12 = pr_12 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера NolimitCity
@router.callback_query(F.data == 'del12')
async def del12(call: types.CallbackQuery):
    button_number = int('del12'[3:])
    button_number_1 = int('btn12'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: NolimitCity',reply_markup=slots)
    await call.message.delete()

#BGaming
@router.callback_query(F.data == 'btn13')
async def btn13(call: types.CallbackQuery, state: FSMContext):
    my_list_BGaming = ['Keepers of the Secret', 'Wild Tiger', 'Hottest 666', 'Jackpot Terminal', 'Gemza', 'Slot Machine', 'Tramp Day', 'Book of Panda MEGAWAYS', 'Mummy’s Gold', 'Merge Up', 'Monster Hunt', 'Mice & Magic Wonder Spin', 'Bone Bonanza', 'Maneki 88 Fortunes', 'Wild Cash Dice', 'Savage Buffalo Spirit MEGAWAYS', 'Dice Million', 'Luck & Magic', 'Dice Bonanza', 'Beast Band', 'Wild Chicago', 'Gemhalla', 'Savage Buffalo Spirit', 'Lucky Crew', 'Royal High-Road', 'Alien Fruits', 'Easter Heist', 'Book of Kemet', 'Lucky Oak', 'Sweet Rush MEGAWAYS', 'Potion Spells', 'Domnitors Treasure', 'Gift Rush', 'Gangsterz', 'Burning Chilli X', 'Soccermania', 'Book of Cats MEGAWAYS', 'Elvis Frog TRUEWAYS', 'Halloween Bonanza', 'Beer Bonanza', 'Forty Fruity Million', 'Wild Cash x9990', 'Maneki 88 Gold', 'Miss Cherry Fruits Jackpot Party', 'Winz to the Moon', 'Lady Wolf Moon Megaways', 'Gold Rush With Johnny Cash', 'Big Atlantis Frenzy', 'Penny Pelican', 'Wild Cash', 'Lucky Farm Bonanza', 'Joker Queen', 'Clover Bonanza', 'Aztec Magic Bonanza', 'Aztec Magic Megaways', 'Bonanza Billion', 'Lucky Dama Muerta', 'Candy Monsta', 'Miss Cherry Fruits', 'Dragon’s Gold 100', 'Aloha King Elvis', 'Dig Dig Digger', 
    'Bitstarz Billion', 'Lady Wolf Moon', 'Fruit Million', 'Hit The Route', 'Johnny Cash', 'Book Of Cats', 'Elvis Frog in Vegas', 'Avalon: The Lost Kingdom', 'Deep Sea', 'Spin and Spell', 'Journey Flirt', 'Mechanical Orange', 'Bob’s Coffee Shop', 'Fantasy Park', 'Fire Lightning', 'Aztec Magic Deluxe', 'Desert Treasure', 'Lucky Blue', 'Domnitors', 'West Town', 'Slotomon Go', 'Lucky Lady Clover', 'Lucky Sweets', 'Hawaii Cocktails', 'Princess Of Sky', 'Scroll Of Adventure', 'Aztec Magic', 'Cherry Fiesta', 'Book Of Pyramids', 'Princess Royal', 'Brave Viking', 'Platinum Lightning Deluxe', 'Road 2 Riches']
    random_my_list_BGaming = random.choice(my_list_BGaming)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: BGaming\nСлот: <code>{random_my_list_BGaming}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn13_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_13 = pr_13 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_13 = pr_13 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера BGaming
@router.callback_query(F.data == 'del13')
async def del13(call: types.CallbackQuery):
    button_number = int('del13'[3:])
    button_number_1 = int('btn13'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: BGaming',reply_markup=slots)
    await call.message.delete()

#Endorphina
@router.callback_query(F.data == 'btn14')
async def btn14(call: types.CallbackQuery, state: FSMContext):
    my_list_Endorphina = ['Santa’s Puzzle', 'Hot Puzzle', 'Book of Brawlers', 'Royal Xmass 2', 'Dia de Los Muertos 2', 'Lucky Streak X', 'Fresh Crush', 'Argonauts', 'Late Night Win', 'Lord Of The Seas', 'Giant Wild Goose Pagoda', 'Green Slot', 'Silk Road', 'Multistar Fruits', 'Joker Ra', 'Cash Streak', '2023 Hit Slot', 'Riches of Caliph', 'Blue Slot', 'Rabbits, Rabbits, Rabbits!', 'Santa’s Gift', 'The Vampires II', 'Crystal Skull', 'Wild Streak', 'Football:2022', 'Lumber Jack', 'Mongol Treasures 2 Archery Competition', 'The Emirate 2', 'Dynamit Miner', 'Samarkand’s Gold', 'Book of Vlad', 'Glory of Egypt', 'Fisher King', 'Cyber Wolf', 'Lucky Cloverland', '2022 Hit Slot', 'Book of Lady', 'King of Ghosts', 'Wild Love', 'Royal Xmass', 'Water Tiger', 'Solar Eclipse', '3 Thunders', 'Magnum Opus', 'Hell Hot 40', 'Book of Oil', 'Hell Hot 20', 'Akbar & Birbal', 'Fruletta', 'Joker Stoker', 'Lucky Dice 3', 'Rooster Fury', 'Hell Hot 100', '2021 HIT', 'Around the World', 
    'Cricket Heroes', 'Legendary Sumo', 'Gem Blast', 'Cupid', 'Golden Ox', 'Chance Machine 5', 'Diamond Chance', 'Book of Santa', 'Chance Machine 40', '100 Zombies', 'Buffalo 50', 'Chance Machine 20', 'Red Cap', 'Chance Machine 100', 'The Rise of AI', '7 Bonus UP!', 'Asgardians', 'Windy City', 'Troll Haven', '2020 Hit', 'Aus Dem Tal', 'Cash Tank', 'Almighty Sparta', 'Mystery of Eldorado', 'Lucky Dice 2', 'Tribe', 'Ancient Troy', 'Lucky Streak 3', '#Luxurylife', 'Lucky streak 2', 'Sugar Glider', 'Lucky Streak 1', 'Dia de Los Muertos', 'Kamchatka', 'Lucky lands', 'Football Superstar', 'Taboo', 'Little Panda', 'Goddess of War', 'IN JAZZ', '2027 ISS', 'Slotomoji', 'Chunjie', 'Diamond Vapor', 'Voodoo', 'Temple Cats', 'Gladiators', 'Safari', 'Geisha', 'Satoshi’s Secret', 'Minotaurus', 'Macarons', 'Wild Fruits', 'Sparkling Fresh', 'The Emirate', 'Mongol Treasures', 'The King', 'Urartu', 'More Fresh Fruits', 'Retromania', 'Sushi', 'Fresh Fruits', '4 Of A King', 'The Vampires', 'Ultra Fresh', 'Undine’s Deep', 'Chimney Sweep', 'Football', 'Gems & Stones']
    random_my_list_Endorphina = random.choice(my_list_Endorphina)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Endorphina\nСлот: <code>{random_my_list_Endorphina}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn14_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_14 = pr_14 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_14 = pr_14 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Endorphina
@router.callback_query(F.data == 'del14')
async def del14(call: types.CallbackQuery):
    button_number = int('del14'[3:])
    button_number_1 = int('btn14'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Endorphina',reply_markup=slots)
    await call.message.delete()

#Quickspin
@router.callback_query(F.data == 'btn15')
async def btn15(call: types.CallbackQuery, state: FSMContext):
    my_list_QUICKSPIN = ['Sticky Bandits Unchained', 'Book of Yuletide', 'Big Bad Wolf: Pigs of Steel', 'Catrina’s Coins', 'Golden Glyph 3', 'Brooklyn Bootleggers', 'Feasting Fox', 'Cash Truck 2', 'Adventures Beyond Wonderland Magical Maze', 'Dog Town Deal', 'Mine & Melt', 'Book of Inferno', 'Betty Bonkers', 'Scatter Monsters', 'Cash Truck Xmas Delivery', 'Raven Rising', 'Primal Spirits', 'Eastern Emeralds Megaways', 'Spinions Game Day', 'Beastwood', 'Sticky Bandits Trail of Blood', 'Slugger Time', 'Flip Royale', 'Azticons Chaos Clusters', 'Sakura Fortune 2', 'High Street Heist', 'Warp Wreckers Power Glyph', 'Cash Truck', 'Spinions Christmas Party', 'Blue Wizard', 'Book of Duat', 'Reno 7s', 'Wild Harlequin', 'Big Bad Wolf Megaways', 'Sevens High Ultra', 'Cabin Crashers', 'Tigers Glory Ultra', 'Guardian of Athens', 'Golden Glyph 2', 'Sticky Bandits 3 Most Wanted', 'Sinbad', 'Crown of Valor', 'Dinosaur Rage', 'Loco the Monkey', 'Big Bad Wolf Christmas Special', 'Crystal Prince', 'Titan Thunder: Wrath of Hades', 'Hammer of Vulcan', 'Ghost Glyph', 'Artemis vs Medusa', 'Arcane Gems', 'Diamond Duke', 'Nero’s Fortune', 'Panthers Reign', 'Wild Cauldron', 'Skulls UP!', 'Polar Paws', 'Golden Glyph', 
    'Wild Chase: Tokyo Go', 'Wild Tome of the Woods', 'Sticky Bandits: Wild Return', 'Prime Zone', 'Dragon Chase', 'Tales of Dr Dolittle', 'Durian Dynamite', 'The Grand', 'Ticket to the Stars', 'Divine Dreams', 'Tiger’s Glory', 'Ark Of Mystery', 'Big Bot Crew', 'Hidden Valley', 'Eastern Emeralds', 'Dwarfs Gone Wild', 'Pirate’s Charm', 'Joker Strike', 'Volcano Riches', 'Northern Sky', 'Pied Piper', 'Rapunzel’s Tower', 'Mighty Arthur', 'Mayana', 'Fairy Gate', 'Sticky Bandits', 'Sakura Fortune', 'Leprechaun Hills', 'Hot Sync', 'Phoenix Sun', 'Dragon Shrine', 'Gold Lab', 'Spinions Beach Party', 'The Wild Chase', 'Genie’s Touch', 'Second Strike', 'Razortooth', 'Crystal Queen', 'Sevens High', 'Illuminous', 'King Colossus', 'Treasure Island', 'Goldilocks and The Wild Bears', 'Big Bad Wolf', 'Hall of the Mountain King', 'Ivan and the Immortal King', 'Vampire Senpai']
    random_my_list_QUICKSPIN = random.choice(my_list_QUICKSPIN)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Quickspin\nСлот: <code>{random_my_list_QUICKSPIN}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn15_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_15 = pr_15 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_15 = pr_15 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Quickspin
@router.callback_query(F.data == 'del15')
async def del15(call: types.CallbackQuery):
    button_number = int('del15'[3:])
    button_number_1 = int('btn15'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Quickspin',reply_markup=slots)
    await call.message.delete()

#Habanero
@router.callback_query(F.data == 'btn16')
async def btn16(call: types.CallbackQuery, state: FSMContext):
    my_list_HABANERO = ['Santa’s Inn', 'Zeus Deluxe', 'Slime Party', 'Meow Janken', 'Bikini Island Deluxe', 'Atomic Kittens', 'Witches Tome', 'Legend of Nezha', 'Tooty Fruity Fruits', 'Crystopia', 'Siren’s Spell', 'The Big Deal Deluxe', 'Naughty Wukong', 'Legendary Beasts', 'Rainbow Mania', 'Dragon Tiger Gate', 'Soju Bomb', 'Tuk Tuk Thailand', 'Taiko Beats', 'Laughing Buddha', 'Space Goonz', 'Golden Unicorn Deluxe', 'Bomb Runner', 'Mighty Medusa', 'Disco Beats', 'Lantern Luck', 'Lucky Durian', 'New Year’ Bash', 'Prost!', 'NineTails', 'Fly!', 'Mystic Fortune Deluxe', 'Calaveras Explosivas', 'Hey Sushi', 'Hot Hot Fruit']
    random_my_list_HABANERO = random.choice(my_list_HABANERO)
    a = random.randint(30, 50)
    b = random.randint(100, 200)
    await call.message.answer(f'Провайдер: Habanero\nСлот: <code>{random_my_list_HABANERO}</code>\nРекомендация по спинам: {a} - 50\nЭкстримальные спины: 50 - {b}', parse_mode='html')
    await call.message.delete()
    time.sleep(1)
    await call.message.answer(f'Введите ваш баланс:')
    await state.set_state(statistics.rate)

@router.message(statistics.rate)
async def btn16_rate(message: Message, state: FSMContext):
    id = message.from_user.id
    await state.update_data(rate=message.text)
    rate = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM users WHERE id={id}")
        if rate.isdigit():
            for row in cursors:
                suma = row['suma']
                if int(rate) >= int(suma):
                    bal = int(rate) - int(suma)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma + {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_16 = pr_16 + {bal} WHERE id = {id}")
                        await message.answer(f"Вы в + на: {bal}\n", reply_markup=slots)
                    connection.commit()
                else:
                    bal = int(suma) - int(rate)
                    with connection.cursor() as cursors:
                        cursors.execute(f"UPDATE users SET suma = suma - {bal} WHERE id = {id}")
                        cursors.execute(f"UPDATE users SET pr_16 = pr_16 - {bal} WHERE id = {id}")
                        await message.answer(f"Вы в - на: {bal}\n", reply_markup=slots)
                    connection.commit()
        else:
            await message.answer("Введите сумму в виде числа:")
            await state.set_state(statistics.rate)
    await state.clear()
    connection.commit()

#удаление провайдера Habanero
@router.callback_query(F.data == 'del16')
async def del16(call: types.CallbackQuery):
    button_number = int('del16'[3:])
    button_number_1 = int('btn16'[3:])
    slots.inline_keyboard[int(button_number) - 1].remove(slots.inline_keyboard[int(button_number) - 1][1])
    slots.inline_keyboard[int(button_number_1) - 1].remove(slots.inline_keyboard[int(button_number_1) - 1][0])
    await call.message.answer('Вы успешно удалили провайдер: Habanero',reply_markup=slots)
    await call.message.delete()
    
#Востановить кнопки
@router.callback_query(F.data == 'btn17')
async def btn17(call: types.CallbackQuery):
    restored_btn1 = InlineKeyboardButton(text="3 Oaks Gaming", callback_data="btn1")
    restored_del1 = InlineKeyboardButton(text="Удалить", callback_data="del1")
    button_btn1 = int('btn1'[3:]) - 1
    button_del1 = int('del1'[3:]) - 1
    restored_btn2 = InlineKeyboardButton(text="PragmaticPlay", callback_data="btn2")
    restored_del2 = InlineKeyboardButton(text="Удалить", callback_data="del2")
    button_btn2 = int('btn2'[3:]) - 1
    button_del2 = int('del2'[3:]) - 1
    restored_btn3 = InlineKeyboardButton(text="BetSoft", callback_data="btn3")
    restored_del3 = InlineKeyboardButton(text="Удалить", callback_data="del3")
    button_btn3 = int('btn3'[3:]) - 1
    button_del3 = int('del3'[3:]) - 1
    restored_btn4 = InlineKeyboardButton(text="Red Tiger", callback_data="btn4")
    restored_del4 = InlineKeyboardButton(text="Удалить", callback_data="del4")
    button_btn4 = int('btn4'[3:]) - 1
    button_del4 = int('del4'[3:]) - 1
    restored_btn5 = InlineKeyboardButton(text="Big Time Gaming", callback_data="btn5")
    restored_del5 = InlineKeyboardButton(text="Удалить", callback_data="del5")
    button_btn5 = int('btn5'[3:]) - 1
    button_del5 = int('del5'[3:]) - 1
    restored_btn6 = InlineKeyboardButton(text="Relax Gaming", callback_data="btn6")
    restored_del6 = InlineKeyboardButton(text="Удалить", callback_data="del6")
    button_btn6 = int('btn6'[3:]) - 1
    button_del6 = int('del6'[3:]) - 1
    restored_btn7 = InlineKeyboardButton(text="Play'n GO", callback_data="btn7")
    restored_del7 = InlineKeyboardButton(text="Удалить", callback_data="del7")
    button_btn7 = int('btn7'[3:]) - 1
    button_del7 = int('del7'[3:]) - 1
    restored_btn8 = InlineKeyboardButton(text="Playson", callback_data="btn8")
    restored_del8 = InlineKeyboardButton(text="Удалить", callback_data="del8")
    button_btn8 = int('btn8'[3:]) - 1
    button_del8 = int('del8'[3:]) - 1
    restored_btn9 = InlineKeyboardButton(text="Wazdan", callback_data="btn9")
    restored_del9 = InlineKeyboardButton(text="Удалить", callback_data="del9")
    button_btn9 = int('btn9'[3:]) - 1
    button_del9 = int('del9'[3:]) - 1
    restored_btn10 = InlineKeyboardButton(text="Amatic", callback_data="btn10")
    restored_del10 = InlineKeyboardButton(text="Удалить", callback_data="del10")
    button_btn10 = int('btn10'[3:]) - 1
    button_del10 = int('del10'[3:]) - 1
    restored_btn11 = InlineKeyboardButton(text="Yggdrasil", callback_data="btn11")
    restored_del11 = InlineKeyboardButton(text="Удалить", callback_data="del11")
    button_btn11 = int('btn11'[3:]) - 1
    button_del11 = int('del11'[3:]) - 1
    restored_btn12 = InlineKeyboardButton(text="NolimitCity", callback_data="btn12")
    restored_del12 = InlineKeyboardButton(text="Удалить", callback_data="del12")
    button_btn12 = int('btn12'[3:]) - 1
    button_del12 = int('del12'[3:]) - 1
    restored_btn13 = InlineKeyboardButton(text="BGaming", callback_data="btn13")
    restored_del13 = InlineKeyboardButton(text="Удалить", callback_data="del13")
    button_btn13 = int('btn13'[3:]) - 1
    button_del13 = int('del13'[3:]) - 1
    restored_btn14 = InlineKeyboardButton(text="Endorphina", callback_data="btn14")
    restored_del14 = InlineKeyboardButton(text="Удалить", callback_data="del14")
    button_btn14 = int('btn14'[3:]) - 1
    button_del14 = int('del14'[3:]) - 1
    restored_btn15 = InlineKeyboardButton(text="Quickspin", callback_data="btn15")
    restored_del15 = InlineKeyboardButton(text="Удалить", callback_data="del15")
    button_btn15 = int('btn15'[3:]) - 1
    button_del15 = int('del15'[3:]) - 1
    restored_btn16 = InlineKeyboardButton(text="Habanero", callback_data="btn16")
    restored_del16 = InlineKeyboardButton(text="Удалить", callback_data="del16")
    button_btn16 = int('btn16'[3:]) - 1
    button_del16 = int('del16'[3:]) - 1
    if slots.inline_keyboard[button_btn1] == []:
        slots.inline_keyboard[button_btn1].insert(1, restored_btn1)
        slots.inline_keyboard[button_del1].insert(1, restored_del1)
    elif slots.inline_keyboard[button_btn2] == []:
        slots.inline_keyboard[button_btn2].insert(1, restored_btn2)
        slots.inline_keyboard[button_del2].insert(1, restored_del2)
    elif slots.inline_keyboard[button_btn3] == []:
        slots.inline_keyboard[button_btn3].insert(1, restored_btn3)
        slots.inline_keyboard[button_del3].insert(1, restored_del3)
    elif slots.inline_keyboard[button_btn4] == []:
        slots.inline_keyboard[button_btn4].insert(1, restored_btn4)
        slots.inline_keyboard[button_del4].insert(1, restored_del4)
    elif slots.inline_keyboard[button_btn5] == []:
        slots.inline_keyboard[button_btn5].insert(1, restored_btn5)
        slots.inline_keyboard[button_del5].insert(1, restored_del5)
    elif slots.inline_keyboard[button_btn6] == []:
        slots.inline_keyboard[button_btn6].insert(1, restored_btn6)
        slots.inline_keyboard[button_del6].insert(1, restored_del6)
    elif slots.inline_keyboard[button_btn7] == []:
        slots.inline_keyboard[button_btn7].insert(1, restored_btn7)
        slots.inline_keyboard[button_del7].insert(1, restored_del7)
    elif slots.inline_keyboard[button_btn8] == []:
        slots.inline_keyboard[button_btn8].insert(1, restored_btn8)
        slots.inline_keyboard[button_del8].insert(1, restored_del8)
    elif slots.inline_keyboard[button_btn9] == []:
        slots.inline_keyboard[button_btn9].insert(1, restored_btn9)
        slots.inline_keyboard[button_del9].insert(1, restored_del9)
    elif slots.inline_keyboard[button_btn10] == []:
        slots.inline_keyboard[button_btn10].insert(1, restored_btn10)
        slots.inline_keyboard[button_del10].insert(1, restored_del10)
    elif slots.inline_keyboard[button_btn11] == []:
        slots.inline_keyboard[button_btn11].insert(1, restored_btn11)
        slots.inline_keyboard[button_del11].insert(1, restored_del11)
    elif slots.inline_keyboard[button_btn12] == []:
        slots.inline_keyboard[button_btn12].insert(1, restored_btn12)
        slots.inline_keyboard[button_del12].insert(1, restored_del12)
    elif slots.inline_keyboard[button_btn13] == []:
        slots.inline_keyboard[button_btn13].insert(1, restored_btn13)
        slots.inline_keyboard[button_del13].insert(1, restored_del13)
    elif slots.inline_keyboard[button_btn14] == []:
        slots.inline_keyboard[button_btn14].insert(1, restored_btn14)
        slots.inline_keyboard[button_del14].insert(1, restored_del14)
    elif slots.inline_keyboard[button_btn15] == []:
        slots.inline_keyboard[button_btn15].insert(1, restored_btn15)
        slots.inline_keyboard[button_del15].insert(1, restored_del15)
    elif slots.inline_keyboard[button_btn16] == []:
        slots.inline_keyboard[button_btn16].insert(1, restored_btn16)
        slots.inline_keyboard[button_del16].insert(1, restored_del16)
        
    await call.message.answer(f'Все кнопки востановлены', parse_mode='html',reply_markup = slots)
    await call.message.delete()

async def send_channel_message(id,bot):
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT SUM(pr_1),SUM(pr_2),SUM(pr_3),SUM(pr_4),SUM(pr_5),SUM(pr_6),SUM(pr_7),SUM(pr_8),SUM(pr_9),SUM(pr_10),SUM(pr_11),SUM(pr_12),SUM(pr_13),SUM(pr_14),SUM(pr_15),SUM(pr_16) FROM users")
        result = cursors.fetchone()
        chat_id = '@searchslot'
        pr_1 = result['SUM(pr_1)']
        pr_2 = result['SUM(pr_2)']
        pr_3 = result['SUM(pr_3)']
        pr_4 = result['SUM(pr_4)']
        pr_5 = result['SUM(pr_5)']
        pr_6 = result['SUM(pr_6)']
        pr_7 = result['SUM(pr_7)']
        pr_8 = result['SUM(pr_8)']
        pr_9 = result['SUM(pr_9)']
        pr_10 = result['SUM(pr_10)']
        pr_11 = result['SUM(pr_11)']
        pr_12 = result['SUM(pr_12)']
        pr_13 = result['SUM(pr_13)']
        pr_14 = result['SUM(pr_14)']
        pr_15 = result['SUM(pr_15)']
        pr_16 = result['SUM(pr_16)']
        chat_member = await bot.get_chat_member('@searchslot',id)
        if chat_member.status == 'member' or chat_member.status == 'administrator' or chat_member.status == 'creator':
            await bot.send_message(chat_id, f'Статистика за 24 часа:\n3 Oaks Gaming: {pr_1}\nPragmaticPlay: {pr_2}\nBetSoft: {pr_3}\nRed Tiger: {pr_4}\nBig Time Gaming: {pr_5}\nRelax Gaming: {pr_6}\nPlay`n GO: {pr_7}\nPlayson: {pr_8}\nWazdan: {pr_9}\nAmatic: {pr_10}\nYggdrasil: {pr_11}\nNolimitCity: {pr_12}\nBGaming: {pr_13}\nEndorphina: {pr_14}\nQuickspin: {pr_15}\nHabanero: {pr_16}')
        else:
            await bot.send_message(id,'Вcтупите в наш канал для просмотра статистики и новостей', reply_markup=canal)
    connection.commit()

def setup(bot,id):
    scheduler.add_job(send_channel_message, 'cron', hour=00, minute=00, args={id,bot})
    scheduler.start()





    # scheduler.add_job(send_channel_message, 'interval', seconds=3, args=[bot])
    # scheduler.add_job(send_channel_message, 'cron', hour=22, minute=28, kwargs={"message": msg,"bot": bot})