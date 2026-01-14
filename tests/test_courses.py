import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        # 1 СЕССИЯ
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем форму рег.
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        # Нажимаем на кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохранение состояния сессии в файл
        context.storage_state(path="browser-state.json")

        # Закрываем первую сессию
        context.close()
        browser.close()


        # 2 СЕССИЯ
        browser2 = playwright.chromium.launch(headless=False)
        # Загружаем состояние из файла
        context2 = browser2.new_context(storage_state="browser-state.json")
        page2 = context2.new_page()

        # Переход на страницу курсов (без повторной авторизации)
        page2.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Заголовок "Courses"
        courses_title = page2.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        # Иконка "Пустая папка"
        empty_view_icon = page2.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_view_icon).to_be_visible()

        # Текст "There is no results"
        no_results_text = page2.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_text).to_be_visible()
        expect(no_results_text).to_have_text("There is no results")

        # Описание
        results_from_text = page2.get_by_test_id('courses-list-empty-view-description-text')
        expect(results_from_text).to_be_visible()
        expect(results_from_text).to_have_text("Results from the load test pipeline will be displayed here")

        browser2.close()