d = int(input('Enter you birth date : '))
m = int(input('Enter your birth month : '))
y = int(input('Enter your birth year : '))

d1 = 0
while d != 0:
    d1 = d1+d % 10
    d = d//10

m1 = 0
while m != 0:
    m1 = m1+m % 10
    m = m//10

y1 = 0
while y != 0:
    y1 = y1+y % 10
    y = y//10

y2 = 0
if y1 > 9:
    while y1 != 0:
        y2 = y2+y1 % 10
        y1 = y1//10
    y1 = y2

t = d1+m1+y1
if t > 9:
    t1 = 0
    while t != 0:
        t1 = t1+t % 10
        t = t//10
    t = t1

if t == 1:
    print('People with the life path number 1 are trailblazers, leaders, and pioneers, going boldly where other numbers wouldn’t dare. They are self-centered,bossy,egotistical')
if t == 2:
    print(' As a 2, you are empathetic and incredibly sensitive to the people around you. You are always looking for harmony, so it goes without saying that you are a peacekeeper and an excellent mediator. As a 2 you are over-emotional,overly sensitive,passive-aggressive')
if t == 3:
    print('People who are 3s can best be described as exceptionally gifted, scatter-brained teenagers who need constant guidance. They are also creative, sharp-witted, and charming, and as if that wasn’t enough, they are also usually blessed with good looks. As a 3s you are Restless,Irresponsible,Non-communicative')
if t == 4:
    print('As a 4, your approach to life is a down-to-earth one, and your personality can best be described as driven with a steel-like determination. As a 4 you are Dull, Stubborn, Close minded, Rude')
if t == 5:
    print('People with the life path number 5 are adventurous with an intrinsic need for freedom. As a 5 you are Reckless, Vain, impatient')
if t == 6:
    print('people with life path number 6 are nurturers who take on the responsibility of others. This motherly number is caring, loving, reliable, and incredibly understanding, with a strong desire to love and be loved. As a 6 you are Unpractical, Hypocritical, Submissive')
if t == 7:
    print(' people with a 7 life path are truth seekers. Seven is a very spiritual number, so they delve into life’s mysteries and things yet unknown. As a 7 you are Selfish, Hermit')
if t == 8:
    print('People with an 8 life path are the boss. They’re powerful people, particularly in their careers, where they are true commanders. These leaders are excellent at making money. As a 8 you are Too proud to take advice, Controlling, Unwilling to co-operate')
if t == 9:
    print('Life path number 9s are humanitarians and philanthropists, and their life number contains the wisdom of numbers 1-8 too. As a 9 you are Being taken advantage of, Emotional mood swings, Oversensitivity')
if t == 11:
    print('Life path 11s are 1 + 1 = 2, so they share the empathetic, emotional, and peace-making characteristics of life path 2s with a spiritual element. As a 11 you are Self-critical, Prone to depression and anxiety, Addicted')
if t == 22:
    print('Life path 22s are the numbers 2 + 2 = 4, so they share the systematic, tenacious, and rational characteristics of the number 4 with a spiritual understanding. As a 22 you are Controlling, Manipulative, Inflexible')
if t == 33:
    print('33 has mastered the ability to be truly selfless.The meaning of life for 33 life path is closely linked with a desire to help others by nurturing and giving. As a 33 you are Controlling, Have very high moral standards')
