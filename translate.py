import i18n

def translate():
    i18n.set('locale', 'sg')
    i18n.set('fallback', 'zh')
    i18n.load_path.append('/Users/aniamritapc/PycharmProjects/pythonProject7')
    print(i18n.t('foo.hi'))  # Hello world !


translate()
