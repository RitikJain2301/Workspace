from playwright.sync_api import Playwright, sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.google.com/")
    page.locator(".SDkEP").click()
    page.get_by_role("combobox", name="Search").fill("khabarein by rap junkie")
    page.get_by_role("combobox", name="Search").press("Enter")
    page.get_by_role("link").filter(has_text="3:18").click()
    page.get_by_role("link", name="Khabarein, YouTube, Rap Junkie - Topic").click()
    page.goto("https://www.youtube.com/watch?v=kqPjyCtu-u8")
    page.get_by_role("link", name="YouTube Home").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path = "trace")


# with sync_playwright() as playwright:
#     run(playwright)
