from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://maskarad-grim.ru/
    page.goto("https://maskarad-grim.ru/")
    # Click header >> text=Вход / Регистрация
    page.locator("header >> text=Вход / Регистрация").click()
    page.wait_for_url("https://maskarad-grim.ru/client_account/login")
    # Click text=Зарегистрироваться
    page.locator("text=Зарегистрироваться").click()
    page.wait_for_url("https://maskarad-grim.ru/client_account/contacts/new")
    # Click input[name="client\[name\]"]
    page.locator("input[name=\"client\\[name\\]\"]").click()
    # Fill input[name="client\[name\]"]
    page.locator("input[name=\"client\\[name\\]\"]").fill("Дарья")
    # Click input[name="client\[surname\]"]
    page.locator("input[name=\"client\\[surname\\]\"]").click()
    # Fill input[name="client\[surname\]"]
    page.locator("input[name=\"client\\[surname\\]\"]").fill("Лебедева")
    # Click input[name="client\[phone\]"]
    page.locator("input[name=\"client\\[phone\\]\"]").click()
    # Click input[name="client\[email\]"]
    page.locator("input[name=\"client\\[email\\]\"]").click()
    # Fill input[name="client\[email\]"]
    page.locator("input[name=\"client\\[email\\]\"]").fill("dare.lebedeva@gmail.com")
    # Click input[name="client\[password\]"]
    page.locator("input[name=\"client\\[password\\]\"]").click()
    # Fill input[name="client\[password\]"]
    page.locator("input[name=\"client\\[password\\]\"]").fill("5646446Ter")
    # Click input[name="client\[password_confirmation\]"]
    page.locator("input[name=\"client\\[password_confirmation\\]\"]").click()
    # Fill input[name="client\[password_confirmation\]"]
    page.locator("input[name=\"client\\[password_confirmation\\]\"]").fill("5646446Ter")
    # Click span[role="checkbox"]
    page.frame_locator("iframe[role=\"presentation\"]").locator("span[role=\"checkbox\"]").click()
    # Click text=Зарегистрироваться
    page.locator("text=Зарегистрироваться").click()
    page.wait_for_url("https://maskarad-grim.ru/client_account/contacts")
    # Click text=У меня уже есть аккаунт
    page.locator("text=У меня уже есть аккаунт").click()
    page.wait_for_url("https://maskarad-grim.ru/client_account/session/new")
    # Click input[name="email"]
    page.locator("input[name=\"email\"]").click()
    # Fill input[name="email"]
    page.locator("input[name=\"email\"]").fill("dare.lebedeva@gmail.com")
    # Click input[name="password"]
    page.locator("input[name=\"password\"]").click()
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("5646446Ter")
    # Press Enter
    page.locator("input[name=\"password\"]").press("Enter")
    page.wait_for_url("https://maskarad-grim.ru/client_account/session")
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
