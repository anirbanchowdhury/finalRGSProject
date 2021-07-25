import i18n


i18n.load_path.append('/Users/aniamritapc/PycharmProjects/pythonProject7')

def load_lang_pref(lang_pref):

    i18n.set('locale', 'sg')
    if lang_pref == 1:
        i18n.set('fallback', 'en')
    elif lang_pref == 2:
        i18n.set('fallback', 'zh')
    elif lang_pref == 3:
        i18n.set('fallback', 'ml')
    else :
        i18n.set('fallback', 'en')
    print(i18n.t('translate.hi'))


load_lang_pref(1)
load_lang_pref(2)
load_lang_pref(3)