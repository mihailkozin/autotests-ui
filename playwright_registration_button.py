from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка registration не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Устанавливаем фокус на поле Email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in 'user@gmail.com':
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.press(character, delay=300)

    # Устанавливаем фокус на поле Username
    email_input = page.get_by_test_id('registration-form-username-input').locator('input')
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in 'username':
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.press(character, delay=300)

        # Устанавливаем фокус на поле Password
    email_input = page.get_by_test_id('registration-form-password-input').locator('input')
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in 'password':
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.press(character, delay=300)

    # Проверяем, что кнопка registration активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()

