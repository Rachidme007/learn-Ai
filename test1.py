# ----------------------------
# Informaton about the file  |
# Liecense                   |
# who Created The File       |
# When The file Created      |
# Why The file Created       |
# ----------------------------
# Type(),and all data in python is Object كائن
print("I ,Back to you")
# <---> print("hi")  Indentation (الفراغات البادئة)

#############################################################
# a => append ===> "إضافة عنصر إلى نهاية القائمة"
# w => write ===> "كتابة بيانات في ملف (يمسح السابق)ة"
# r => read ===> "قراءة محتوى الملف	"
print(type([1, 2, 3, 4, 5]))  # list
print(type((1, 2, 3, 4, 5)))  # tuple
print(type({"One": 1}))
##############################################################
# لدى بايثون كلمات محجوزة RESERVED WORDS
# help("keywords")
# --------------------------------------------------------------
# Escape sequances characters
# \b       ==>Back space سيتم حذف الحر الذي قبلها
# \newline ==> Escape new line + \ حتى لو صنعت سطر جديد فستجعله بدون مشاكل
# \\       ==> escape back slash تعكس وضيفتها للتعرض نفسها
# \ "      ==> escape quote  تعمس مايحدث لل"
# \n       ==> line feed سطر جديد
# \r       ==> carriage return تاخذ الكلمة التى بعدها وتكتبها وتضيف ماكان قبلها بعدد حروف الكلمة التى بعدها
# \t       ==> horizontal Tab يعمل tab
# \xhh      ==> hex value characters

# ===============================================================
# --------------------------------------------------------------
# String Indexing & Slicing
# [1] ALL DATA IN PYTHON IS OBJECT  كل البيانات في بايثون تُعتبر كائنات (Objects)، سواء كانت أرقامًا أو نصوصًا أو قوائم أو غيرها
# [2] OBJECT CONTAIN ELEMENTS 🔸 الكائنات مثل السلاسل النصية والقوائم يمكن أن تحتوي على عناصر داخلها.
# [3] EVERY ELEMENTS HA ITS OWN INDEX  كل عنصر داخل تسلسل (مثل قائمة أو سلسلة) له رقم فهرسة (Index) خاص به يُستخدم للوصول إليه.
# [4] PYTHON USE ZERO BASED INDEX (INDEX START FROM ZER)  بايثون تستخدم نظام فهرسة يبدأ من الصفر، أي أن أول عنصر يكون رقمه 0
# [5] USE SQUARE  BRACKETS TO ACCES ELEME  يتم استخدام الأقواس المربعة [ ] للوصول إلى العناصر داخل الكائنات القابلة للفهرسة.
# [6] Enables accessing parts of strings, tuples,  slicing يمكن الوصول إلى جزء من سلسلة نصية أو قائمة أو صف باستخدام تقنية التقطيع (slicing) بصيغة start:stop:step.


# ===============================================================
# --------------------------------------------------------------
# -----------Strings Methods-----------                         |
# _______print(var.method())                                    |
# len()   counting charachters                                  |
# rstrip(WHAT YOU WANT TO REMOVE) مسح المسافات من اليمين       |
# Strip() مسح المسافات من اليسار                               |
# strip() مسح المسافات من كلا الجهتين                           |
# Title() تحويل الجمل الى  first capitale                       |
# CAPITALIZE() تحويل الجمل الى  باستثناء بعد الرقام capitale  |
# zfill(رقم) اضافة الصفر الى بداية الارقام                     |
# Upper()                                                        |
# Lower()                                                        |
# split(الرقم الذي سياخذ بيه,المرجع الذي سيقسم بيه) تحول المتغير الى list
# rsplitنفس العمل لكن من اليمين
# center( الرمز الذي ستزيت بيه ,عدد الاحرف التي سترجع) تكت بعدوقبل النص
# COUNT(الحرق الذي كم سيتكر,من,الى) تحسب عذد CHARACHTERS
# SWAPECASE()يغير الحرف كيفما تريد او يعكس
# STARTSWTH("ANY",FROM,TO) هل يبدا بحرف كذا ويرجع BOOL
# ENDWITH()عكسها
# Index(Substring,Start,END) تجدد لك اين يوجد الحرف الذي تبحث عنه
# find(Substring,Start,END)) تختلف انها تعطيك -1 بدل error
# ljust(WIDTH,FILL CHAR)تملئ الحروف بقدر وتحديد ماتدخل
# rjust(WIDTH,FILL CHAR)
# Splitlines()ترجع السطور \N الى LIST
# Expandtabs()تأخذ \T وتترك تتحكم في مقدار مسافتها
# Istitle() هل كل بدايو ي النص حرف كبير
# ispace() هل هو مسافة
# islower()
# isidentifier() هل هو معرف ام لا
# isalpha()
# isalnum()
# Email = "rachidmedox@gmail.com"
# user1= Email[: Email.index("@")] تعيط قبل @ من السطر الفوق
# /\/\/\/\/\/\/\/\//\/\/\/\/\/\\
# replace(old VALUE,NEW VALUE,COUNT)
# join()--"".join(listname) ترحع العناصر او الليست STRING
# print("MY NAME IS %.6s ,%d %.2f ," % (a, a)) اسمها place holder
# print("text {:s} {:d}".format(var1,var2))
# {:_d}||{:,d} كل ثلاثة ارقام فاصلة ||
# ReArrange Itemes a,b,c print("text{1} {2} {0}".format(a,b,c)) تختار ان تعير مكانهم ام تتركهم فارغين
# print(f"MyName is {Myname} and {var2}")
# --------------------------------------------------------------
# ===============================================================
# -------------Numbers------
# INT-->1    |Float-->1.00   |Complexe-->1-2j  print(var.real or var.iMAG)  |INT-->     |
# PEMDAS الهام جدًا في المعادلات الرياضية. Parenthesis - Exponentiation
# [*]Multiplication
# [/]Division
# [+]Adding
# [-]Subtracting.
# [%]Moduls
# [**]exponent الاس ^
# [//]Floor Divisiom هل تقبل الفسمة

# -------------lISTS------
# [1] List Items Are Enclosed in Square Brackets
# [2]List Are Ordered from 0
# [3] mutable to add delet edit
# [4]items is not unique
# [5]list can have different data types
# print([mylist[1:4]) form 1 to 3
# print([mylist[:4]) form begin to 3
# print([mylist[::2]) jump by 1
# VARLIST.append("") تضيف الى القائمة
# LST1.extend(list2) دمج الlist
# LIST1.remove("") تمسح
# list.sort() list.sort(reverse=false) KEY=LEN or str ـرتيب
# list1.clear()
# lst2=list1.Copy()
# list1.count()
# list.index("words")
# list1.insert(0,"add this")
# list1.Pop(-5)

# ===============================================================
# --------------------------------------------------------------
# -------------Tuples------مثل list لكن اكثر ملائمة
# [1] Tuple Items Are enclosed in parents ()
# [2] you can remove the parentheses if you want
# [3]tuple are orderd to use indexing to  acces items
# [4] tuple are immutabele you cant add or delete
# [5]tuple items not unique
# [6] you can have different Data type
# [7]operatots used in string and lists Availables in tuples
# =========
# tuple with one element tupl1="sti",
# tuple  concatenation
# Tuple,list,string Repat * you can multiple it
# tuples.count() methos => count( )
# tuples.index() methos => index(4)
# Tuples Destruct x,y,_,z=tuple1

# ===========================

# ╔═━═━═━═━═━═━═━═━═━═══━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═══━═━═━═══━═━═━═━═━══╗
# ║ 🚀 M E T H O D   N A M E : 🔴 SET 🔴               ║
# ╚═━═━═━═════━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═╝
#  ➡️ [1] SET ITEMS ARE NOT ENCLOSED IN CURLY BRACES{}
#  ➡️ [2] SET ITEMS ARE NOT ORDERDED NOT INDEXED
#  ➡️ [3] ST INDEXING AND SLICING CANT BE DONE
#  ➡️ [4] set can only contain immutable data types (numbers, tuples, string) and not dic list
#  ➡️ [5] set items must be unique
#      set1.clear
#           .union() or st1 |set2 أتحاد
#           .add(num1) تضيف عنصر
#           .copy()
#           .remove(num1) طلع خظأ اذا مو موجود
#           .discard(num2) لانظهر خطا
#           .pop() يطلع او يطبع جزء عشوائي
#           .update(set2/"string") يدمج مثل union ولكن لايكرر ماهو مكرر
#           .Difference(set2)
#           .diffrenece_update / symmetric_difference()
#           .intersection(set2) عكس الدالةفوقها
#           .intersection_update(set2) يحفظهم في اذالة الاولى
#           .issuperset(set2) هل تشبه الثانية الاولى كليا
#           .issubset(set2) هل لاتشبها كليا عكس الدالة الاولى
#           .isdisjoint(set2) هل منفصلين عن بعض لايتشابهون
# =============================================================================
# END: [METHOD]
# =============================================================================

# ╔═━═━═━═━═━═━═━═━═━═══━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═══━═━═━═══━═━═━═━═━══╗
# ║ 🚀 M E T H O D   N A M E : 🔴 Dictionary🔴               ║
# ╚═━═━═━═════━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═╝
#  ➡️ [1] Dict items are inclosed in braces {}
#  ➡️ [2] Dict items are contains key:value
#  ➡️ [3] Dict Key Need to be Immutable => (Number,string,Tuples) lists not Allowed
#  ➡️ [4] DICT Value can have any Data types
#  ➡️ [5] Dict key need To Be Unique
#  ➡️ [6] Dict Is Not Ordered You Acces Its Element With Key
#      dict1.Keys()
#           .Values()
#           can have nested dictionary
#           .clear لمحو مايوجد في الدالة
#           .update({"key":"value"}) تضيف
#     dic2= .copy() من الاسم نسخ
#           .setdefault("key":"value") لو وجد value او key شبه في dict1 سيعطيك مقابلها ولو ماوجد شئ سيظيفه
#           .popitem() بيعيط اخر حاجة اضافت
#        var=view.items() تحتفظ بكل التغييرات على dict قبل وبعد
#       dict.fromkeys(dictkeys,dictvalue) يضيف value الى key
# =============================================================================
# END: [METHOD]
# =============================================================================
# ╔═━═━═━═━═━═━═━═━═━═══━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═══━═━═━═══━═━═━═━═━══╗
# ║ 🚀 M E T H O D   N A M E : 🔴 Operators🔴                              ║
# ╚═━═━═━═════━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━════╝
#                               Boolean
#  ➡️[1]In Programmin You Need To Konw IF You Code Output Is True Or False
#  ➡️[2]Boolean Values Are The Two Constant Objects False + True
#        var.isspace() هل يحتوي على مسافة
#        num<>+-/%==
#          Bool() معرفة الحالة true false
#         logical = None,not فقك للتذكير ليس لها علاقة
#
#                                 Assignment
#           -=
#           +=
#           /=
#          **=
#           %=
#           *=
#           //=
#                                 Comparison
#
#           [==] Equal
#           [!=] not Equal
#           [>] Greater Than
#           [>] Less Than
#           [>] Greater Than Or Equal
#           [>] Less Than Or Equal

# =============================================================================
# END: [METHOD]
# =============================================================================

# ╔═━═━═━═━═━═━═━═━═━═══━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═══━═━═━═══━═━═━═━═━══╗
# ║ 🚀 M E T H O D   N A M E : 🔴Type Conversion🔴                       ║
# ╚═━═━═━═════━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═╝
#  ➡️
#  ➡️
#           =>str(var)
#           =>tuple(var)
#           =>list(var)
#           ==>Set(var)
#           =>Dict(var)  same thing for set list اذا كنت تحويل   tuple الى dict فيجب ان يكون tuple (("A",1),("C",2))
#           =>list(var)


# -----------------User Input---------------------------------------------
#          var=Input("message")


# =============================================================================
# END: [METHOD]
# =============================================================================
# ╔═━═━═━═━═━═━═━═━═━═══━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═══━═━═━═══━═━═━═━═━══╗
# ║ 🚀 M E T H O D   N A M E : 🔴  Control Flow 🔴                        ║
# ╚═━═━═━═════━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═╝
# --------------------------------- If, Elif, Else-------------------------------
#  ➡️
#  ➡️
#          if == or ==:
#          if : elif: else:
#   nasted if: if
# -----------------Ternary Conditionl operator
# print("your message " if age>agei else your no mesage)
# print ("A" in or not in string)
# =============================================================================
# END: [METHOD]
# =============================================================================
# ╔═━═━═━═━═━═━═━═━═━═══━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═══━═━═━═══━═━═━═━═━══╗
# ║ 🚀 M E T H O D   N A M E : 🔴 LOOP_WHILE🔴                            ║
# ╚═━═━═━═════━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═╝
#  ➡️While Condition is true
#  ➡️ Code wil run

# =============================================================================
# END: [METHOD]
# =============================================================================


#           .


# =============================================================================
# END: [METHOD]
# =============================================================================

# --- Description -----------------------------------------------------------

a = 0
j = a
while a < 10:
    print("*")
    while j < 9:
        print("*")
a += 1


# ╔═━═━═━═━═━═━═━═━═━═══━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═══━═━═━═══━═━═━═━═━══╗
# ║ 🚀 M E T H O D   N A M E : 🔴 authenticate_user_login`🔴               ║
# ╚═━═━═━═════━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═══━═╝
#  ➡️
#  ➡️

# =============================================================================
# END: [METHOD]
# =============================================================================
