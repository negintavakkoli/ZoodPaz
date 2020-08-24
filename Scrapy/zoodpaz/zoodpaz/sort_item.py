import json

with open("recipe.json", "r") as f:
    f = json.load(f)
Ingredient_lsit = []
ii = 0
for item in f:
    recipeIngredient_temp = item["recipeIngredientName"]
    for recipeIngredient in recipeIngredient_temp:

        ii+=1
        # recipeIngredient = recipeIngredient.replace("خرد شده","")
        recipeIngredient = recipeIngredient.replace ( " سولیکو" , "" )
        recipeIngredient = recipeIngredient.replace ( " کاله" , "" )
        recipeIngredient = recipeIngredient.replace ( "سولیکو" , "" )
        recipeIngredient = recipeIngredient.replace(" تازه","")
        # recipeIngredient.replace ( "پمینا" , "" )
        # recipeIngredient.replace ( "آماده" , "" )
        recipeIngredient = recipeIngredient.lstrip ().rstrip ()
        recipeIngredient = recipeIngredient.replace("\u200c" , " ")
        recipeIngredient = recipeIngredient.replace ( "  " , " " )
        if "بیسکویت" in recipeIngredient:
            recipeIngredient = "بیسکویت"
        if (("بیسکوئیت" in recipeIngredient) or ("بیسکویئت" in recipeIngredient)):
            recipeIngredient = "بیسکویت"
        if( ( "برنج" in recipeIngredient) and ("برنجک" not in recipeIngredient) and ("آرد" not in recipeIngredient) and ("سرکه" not in recipeIngredient) and ("قهوه" not in recipeIngredient)):
            recipeIngredient = "برنج"
        if (("بستنی" in recipeIngredient) and ("قیف" not in recipeIngredient)):
            recipeIngredient = "بستنی"
        if (("سبزیجات متناسب (به قطعات" in recipeIngredient)):
            recipeIngredient = "سبزیجات"
        if (("هویج" in recipeIngredient)):
            recipeIngredient = "هویج"
        if (("ماهی " in recipeIngredient) and ("کنسرو" not in recipeIngredient)):
            recipeIngredient = "ماهی"
        if (("فیله ماهی" in recipeIngredient)):
            recipeIngredient = "ماهی"
        if (("فلفل دلمه" in recipeIngredient)):
            recipeIngredient = "فلفل دلمه"
        if (("میگو" in recipeIngredient)):
            recipeIngredient = "میگو"
        if (("گیلاس" in recipeIngredient)):
            recipeIngredient = "گیلاس"
        if (("شیر " in recipeIngredient)):
            recipeIngredient = "شیر"
        if (("لبو" in recipeIngredient)):
            recipeIngredient = "لبو"
        if (("ماست" in recipeIngredient)):
            recipeIngredient = "ماست"
        if (("کره" in recipeIngredient) and ("بادام زمینی" not in recipeIngredient) and ("ماسکارپونه" not in recipeIngredient) and ("کاکائو" not in recipeIngredient)):
            recipeIngredient = "کره"
        if (("گل کلم" in recipeIngredient)):
            recipeIngredient = "گل کلم"
        if (("کلم بروکلی" in recipeIngredient)):
            recipeIngredient = "کلم بروکلی"
        if (("پاستا" in recipeIngredient)):
            recipeIngredient = "پاستا"
        if (("گوجه فرنگی" in recipeIngredient) and ("رب" not in recipeIngredient)):
            recipeIngredient = "گوجه فرنگی"
        if (("تخم مرغ" in recipeIngredient) and ("کیک" not in recipeIngredient)):
            recipeIngredient = "تخم مرغ"
        if (("طالبی" in recipeIngredient)):
            recipeIngredient = "طالبی"
        if (("انواع میوه های رسیده" in recipeIngredient)):
            recipeIngredient = "میوه"
        if (("سیب زمینی" in recipeIngredient)):
            recipeIngredient = "سیب زمینی"
        if (("سیب" in recipeIngredient) and ("زمینی" not in recipeIngredient)):
            recipeIngredient = "سیب"
        if (("سیر" in recipeIngredient) and ("سیروپ" not in recipeIngredient) and ("سیراب" not in recipeIngredient) and ("موسیر" not in recipeIngredient)):
            recipeIngredient = "سیر"
        if (("سیراب" in recipeIngredient)):
            recipeIngredient = "سیراب شیردان"
        if (("کدو حلوایی" in recipeIngredient)):
            recipeIngredient = "کدو حلوایی"
        if (("کدو سبز" in recipeIngredient)):
            recipeIngredient = "کدو سبز"
        if (("کاهو" in recipeIngredient)):
            recipeIngredient = "کاهو"
        if (("هندوانه" in recipeIngredient)):
            recipeIngredient = "هندوانه"
        if (("اسفناج" in recipeIngredient)):
            recipeIngredient = "اسفناج"
        if (("بیسکوییت" in recipeIngredient)):
            recipeIngredient = "بیسکویت"
        if (("خرمالو" in recipeIngredient)):
            recipeIngredient = "خرمالو"
        if (("خرما" in recipeIngredient)):
            recipeIngredient = "خرما"
        if (("انگور" in recipeIngredient) and ("آب" not in recipeIngredient)):
            recipeIngredient = "انگور"
        if (("زردآلو" in recipeIngredient)):
            recipeIngredient = "زردآلو"
        if (("ژله" in recipeIngredient)):
            recipeIngredient = "ژله"
        if (("توت فرنگی" in recipeIngredient) and ("اسانس" not in recipeIngredient)):
            recipeIngredient = "توت فرنگی"
        if (("تن ماهی" in recipeIngredient)):
            recipeIngredient = "تن ماهی"
        if (("کنسرو ماهی تن جوشانده شده" in recipeIngredient)):
            recipeIngredient = "تن ماهی"
        if (("روغن زیتون" in recipeIngredient)):
            recipeIngredient = "روغن زیتون"
        if (("زیتون" in recipeIngredient) and ("روغن" not in recipeIngredient)):
            recipeIngredient = "زیتون"
        if (("زعفران" in recipeIngredient)):
            recipeIngredient = "زعفران"
        if (("شکلات تلخ" in recipeIngredient)):
            recipeIngredient = "شکلات تلخ"
        if (("شکلات تخته ای" in recipeIngredient)):
            recipeIngredient = "شکلات تخته ای"
        if (("پیاز" in recipeIngredient) and ("پیازچه" not in recipeIngredient)):
            recipeIngredient = "پیاز"
        if (("پیازچه" in recipeIngredient)):
            recipeIngredient = "پیازچه"
        if (("چغندر" in recipeIngredient)):
            recipeIngredient = "چغندر"
        if (("به متوسط" in recipeIngredient)):
            recipeIngredient = "به"
        if (("نعنا" in recipeIngredient)):
            recipeIngredient = "نعنا"
        if (("نشاسته" in recipeIngredient)):
            recipeIngredient = "نشاسته"
        if (("بوقلمون" in recipeIngredient)):
            recipeIngredient = "بوقلمون"
        if (("خامه" in recipeIngredient) and ("پنیر" not in recipeIngredient)):
            recipeIngredient = "بوقلمون"
        if (("پنیر خامه" in recipeIngredient)):
            recipeIngredient = "پنیر خامه ای"
        if (("بادمجان" in recipeIngredient)):
            recipeIngredient = "بادمجان"
        if (("آب انار" in recipeIngredient)):
            recipeIngredient = "آب انار"
        if (("آب لیمو" in recipeIngredient)):
            recipeIngredient = "آبلیمو"
        if (("آبلیمو تازه" in recipeIngredient)):
            recipeIngredient = "آبلیمو"
        if (("آبلیموی تازه" in recipeIngredient)):
            recipeIngredient = "آبلیمو"
        if (("آرد گندم" in recipeIngredient)):
            recipeIngredient = "آرد"
        if (("گلوتن" in recipeIngredient) and ("نان سلینو") not in recipeIngredient):
            recipeIngredient = "آرد"
        if (("آرد" in recipeIngredient) and ("بادام" not in recipeIngredient) and ("برنج" not in recipeIngredient) and ("ذرت" not in recipeIngredient) and ("نخودچی" not in recipeIngredient)):
            recipeIngredient = "آرد"
        if (("آرد نخودچی" in recipeIngredient)):
            recipeIngredient = "آرد نخودچی"
        if (("آرد گندم" in recipeIngredient)):
            recipeIngredient = "آرد"
        if (("آلو" in recipeIngredient) and ("برگ" not in recipeIngredient) and ("زردآلو" not in recipeIngredient)):
            recipeIngredient = "آلو"
        if (("هلو" in recipeIngredient)):
            recipeIngredient = "هلو"
        if (("سوسیس" in recipeIngredient)):
            recipeIngredient = "سوسیس"
        if (("ژامبون" in recipeIngredient)):
            recipeIngredient = "ژامبون"
        if (("گلابی سفت و رسیده" in recipeIngredient)):
            recipeIngredient = "گلابی"
        if (("کدو" in recipeIngredient) and ("کدوحلوایی" not in recipeIngredient)):
            recipeIngredient = "کدو"
        if (("کدوحلوایی" in recipeIngredient)):
            recipeIngredient = "کدو حلوایی"
        if (("کرفس" in recipeIngredient)):
            recipeIngredient = "کرفس"
        if (("کالباس" in recipeIngredient)):
            recipeIngredient = "ژامبون"
        if (("نخود" in recipeIngredient) and ("نخودفرنگی" not in recipeIngredient) and ("نخودچی" not in recipeIngredient)):
            recipeIngredient = "نخود"
        if (("نخودفرنگی" in recipeIngredient)):
            recipeIngredient = "نخود فرنگی"
        if (("لازانيا" in recipeIngredient)):
            recipeIngredient = "ورق لازانیا"
        if (("لازانیا" in recipeIngredient)):
            recipeIngredient = "ورق لازانیا"
        if (("نارنگی" in recipeIngredient)):
            recipeIngredient = "نارنگی"
        if (("لوبیا" in recipeIngredient)and ("عروس" not in recipeIngredient) and ("سبز" not in recipeIngredient) and ("سفید" not in recipeIngredient)and ("چیتی" not in recipeIngredient) and ("چشم" not in recipeIngredient)):
            recipeIngredient = "لوبیا قرمز"
        if (("لوبیا سفید" in recipeIngredient)):
            recipeIngredient = "لوبیا سفید"
        if (("لوبیا چشم بلبلی" in recipeIngredient)):
            recipeIngredient = "لوبیا چشم بلبلی"
        if (("لوبیا سبز" in recipeIngredient)):
            recipeIngredient = "لوبیا سبز"
        if (("مخمر" in recipeIngredient)):
            recipeIngredient = "مخمر"
        if (("تره" in recipeIngredient) and ("سبزی" not in recipeIngredient) ):
            recipeIngredient = "تره"
        if (("گشنیز و جعفری" in recipeIngredient)):
            recipeIngredient = "سبزی قرمه"
        if (("سبزیجات" in recipeIngredient)):
            recipeIngredient = "سبزیجات"
        if (("قارچ" in recipeIngredient)):
            recipeIngredient = "قارچ"
        if (("ماکارونی" in recipeIngredient) or ("پنه" in recipeIngredient) or ("اسپاگتی" in recipeIngredient)):
            recipeIngredient = "ماکارونی"
        if (("کنگر" in recipeIngredient)):
            recipeIngredient = "کنگر"
        if (("کوکی" in recipeIngredient)):
            recipeIngredient = "کوکی"
        if (("نان تست" in recipeIngredient)):
            recipeIngredient = "نان تست"
        if (("نان پیتزا" in recipeIngredient)):
            recipeIngredient = "نان پیتزا"
        if (("نان باگت" in recipeIngredient)):
            recipeIngredient = "نان باگت"
        if (("پاناکوتا" in recipeIngredient)):
            recipeIngredient = "پاناکوتا"
        if (("سس مایونز" in recipeIngredient)):
            recipeIngredient = "سس مایونز"
        if (("سویا" in recipeIngredient) and ("سس" not in recipeIngredient)):
            recipeIngredient = "سویا"
        if (("آووکادو" in recipeIngredient)):
            recipeIngredient = "آووکادو"
        if (("بادام زمینی" in recipeIngredient)):
            recipeIngredient = "بادام زمینی"
        if (("گردو" in recipeIngredient)):
            recipeIngredient = "گردو"
        if (("جعفری" in recipeIngredient)):
            recipeIngredient = "جعفری"
        if (("کوکتل" in recipeIngredient) or ("سوجوک" in recipeIngredient) or ("هات داگ" in recipeIngredient) or ("سالامی") in recipeIngredient):
            recipeIngredient = "سوسیس"
        if (("آبمیوه" in recipeIngredient)):
            recipeIngredient = "آبمیوه"
        if (("آب سرد" in recipeIngredient) or ("آب معدنی" in recipeIngredient) or ("آب یا آب" in recipeIngredient) or ("آب ولرم" in recipeIngredient)):
            recipeIngredient = "گردو"
        if (("روغن" in recipeIngredient) and ("زیتون" not in recipeIngredient)):
            recipeIngredient = "روغن"
        if (("ریحان" in recipeIngredient)):
            recipeIngredient = "ریحان"
        if (("لیمو" in recipeIngredient) and ("آبلیمو" not in recipeIngredient) and ("لیموشیرین" not in recipeIngredient) and ("پوست" not in recipeIngredient)):
            recipeIngredient = "لیموترش"
        if (("خمیر مایه" in recipeIngredient)):
            recipeIngredient = "خمیر مایه"
        if (("خمیر هزارلا" in recipeIngredient)):
            recipeIngredient = "خمیر هزارلا"
        if (("خمیر پیتزا" in recipeIngredient)):
            recipeIngredient = "خمیر پیتزا"
        if (("خمیر تارت" in recipeIngredient)):
            recipeIngredient = "خمیر تارت"
        if (("خمیر پیراشکی" in recipeIngredient)):
            recipeIngredient = "خمیر پیراشکی"
        if (("خمیر فیلو" in recipeIngredient)):
            recipeIngredient = "خمیر فیلو"
        if (("خمیر پای" in recipeIngredient)):
            recipeIngredient = "خمیر پای"
        if (("موزارلا" in recipeIngredient) or ("موزرالای" in recipeIngredient)):
            recipeIngredient = "پنیر موزارلا"
        if (("موز " in recipeIngredient)):
            recipeIngredient = "موز"
        if (("پنه" in recipeIngredient)):
            recipeIngredient = "ریحان"
        if (("پنیر کم چرب" in recipeIngredient)):
            recipeIngredient = "پنیر سفید"
        if (("پنیر کبابی" in recipeIngredient)):
            recipeIngredient = "پنیر کبابی"
        if (("گودا" in recipeIngredient)):
            recipeIngredient = "پنیر گودا"
        if (("پنیر فتا" in recipeIngredient)):
            recipeIngredient = "پنیر فتا"
        if (("پنیر سفید" in recipeIngredient)):
            recipeIngredient = "پنیر سفید"
        if (("پودر آب پنیر" in recipeIngredient)):
            recipeIngredient = "آب پنیر"
        if (("پنیر آنا لبنه" in recipeIngredient)):
            recipeIngredient = "پنیر سفید"
        if (("پنیر هالومی" in recipeIngredient)):
            recipeIngredient = "پنیر هالومی"
        if (("سوربن" in recipeIngredient)):
            recipeIngredient = "شکلات"
        if (("شکلات سفید" in recipeIngredient)):
            recipeIngredient = "شکلات سفید"
        if (("پودر نارگیل" in recipeIngredient)):
            recipeIngredient = "پودر نارگیل"
        if (("نارگیل" in recipeIngredient) and ("پودر" not in recipeIngredient)):
            recipeIngredient = "نارگیل"
        if (("گوجه سبز" in recipeIngredient)):
            recipeIngredient = "گوجه سبز"
        if (("چرخ" in recipeIngredient) and ("مرغ چرخ" not in recipeIngredient)):
            recipeIngredient = "گوشت چرخ کرده"
        if (("گوشت راسته" in recipeIngredient)):
            recipeIngredient = "گوشت راسته"
        if (("فیله" in recipeIngredient) and ("گوشت" in recipeIngredient)):
            recipeIngredient = "گوشت فیله"
        if (("گوشت خورشتی" in recipeIngredient)):
            recipeIngredient = "گوشت خورشتی"
        if ( ("گوشت خرد کرده" in recipeIngredient) or ("گوشت ریز خرد" in recipeIngredient) or ("استیک" in recipeIngredient) or ("گوشت قرمز" in recipeIngredient) or ("گوشت با استخوان" in recipeIngredient)  ):
            recipeIngredient = "گوشت گوساله"
        if (("گوشت گردن" in recipeIngredient)):
            recipeIngredient = "گوشت گردن"
        if (("گوسفند" in recipeIngredient)):
            recipeIngredient = "گوشت گوسفندی"
        if ((("گاو" in recipeIngredient) or ("گوساله" in recipeIngredient)) and ("زبان" not in recipeIngredient) ):
            recipeIngredient = "گوشت گوساله"
        if (("سینه" in recipeIngredient)):
            recipeIngredient = "سینه مرغ"
        if (("گوشت مرغ" in recipeIngredient)):
            recipeIngredient = "مرغ"
        if (("ران" in recipeIngredient) and ("مرغ" in recipeIngredient)):
            recipeIngredient = "ران مرغ"
        if (("فیله مرغ" in recipeIngredient)):
            recipeIngredient = "فیله مرغ"
        if (("راغ مرغ" in recipeIngredient)):
            recipeIngredient = "ران مرغ"
        if (("سفیده مرغ" in recipeIngredient) or ("جوجه مرغ" in recipeIngredient) or ("مرغ کامل" in recipeIngredient) or ("تکه های مرغ" in recipeIngredient) or ("مرغ چرخ" in recipeIngredient) or ("مرغ پخته" in recipeIngredient) or ("مرغ سالم" in recipeIngredient) or ("مرغ تکه" in recipeIngredient)):
            recipeIngredient = "مرغ"
        if (("بیکن" in recipeIngredient)):
            recipeIngredient = "بیکن"
        if (("فلفل قرمز" in recipeIngredient)):
            recipeIngredient = "فلفل قرمز"
        if (("کینوا" in recipeIngredient)):
            recipeIngredient = "کینوا"
        if (("قهوه داغ" in recipeIngredient)):
            recipeIngredient = "قهوه"
        if (("شلغم" in recipeIngredient)):
            recipeIngredient = "شلغم"
        if (("شکر سفید" in recipeIngredient)):
            recipeIngredient = "شکر"
        if (("بلغور" in recipeIngredient)):
            recipeIngredient = "بلغور"
        if (("تمشک" in recipeIngredient)):
            recipeIngredient = "تمشک"
        if (("بلوبری" in recipeIngredient)):
            recipeIngredient = "بلوبری"
        if (("بادام آسیاب" in recipeIngredient)):
            recipeIngredient = "بادام"
        if (("بلغور" in recipeIngredient)):
            recipeIngredient = "بلغور"
        if (("پارما" in recipeIngredient)):
            recipeIngredient = "پارمای مرغ"
        if (("پودر ژلاتین" in recipeIngredient)):
            recipeIngredient = "پودر ژلاتین"
        if (("کلم بروکسل" in recipeIngredient)):
            recipeIngredient = "کلم بروکسل"
        if (("کلم بزرگ" in recipeIngredient)):
            recipeIngredient = "کلم"
        if (("کلم پیچ" in recipeIngredient)):
            recipeIngredient = "کلم پیچ"
        if (("خیار" in recipeIngredient)):
            recipeIngredient = "خیار"
        if (("اسطوخودوس" in recipeIngredient) or ("اسطوخدوس" in recipeIngredient)):
            recipeIngredient = "اسطوخودوس"
        if (("ذرت" in recipeIngredient) and ("آرد" not in recipeIngredient)):
            recipeIngredient = "ذرت"
        if (("دال عدس" in recipeIngredient)):
            recipeIngredient = "دال عدس"
        Ingredient_lsit.append(recipeIngredient)
        Ingredient_lsit = list(set(Ingredient_lsit))


with open("Ingredient_lsit.txt", "w") as f:
    json.dump(Ingredient_lsit,f)

print(ii)
Ingredient_lsit.sort()
print(Ingredient_lsit)
print(len(Ingredient_lsit))

