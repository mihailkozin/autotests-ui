import pytest
from playwright.sync_api import expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):

    print("Запускаю страницу с сохраненным состоянием")
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Заголовок "Courses"
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Иконка "Пустая папка"
    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Текст "There is no results"
    no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_visible()
    expect(no_results_text).to_have_text("There is no results")

    # Описание
    results_from_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_from_text).to_be_visible()
    expect(results_from_text).to_have_text("Results from the load test pipeline will be displayed here")
    print("Тест завершен")
