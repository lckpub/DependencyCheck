from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://202.121.180.97:30088/
    page.goto("http://202.121.180.97:30088/")

    # Click text=扫描压缩包或文件
    page.locator("text=扫描压缩包或文件").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/uploader")

    # Click text=点击此处回到主菜单重新上传
    page.locator("text=点击此处回到主菜单重新上传").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/")

    # Click input[name="file"]
    page.locator("input[name=\"file\"]").click()

    # Upload test.rar
    page.locator("input[name=\"file\"]").set_input_files("test.rar")

    # Click text=扫描压缩包或文件
    page.locator("text=扫描压缩包或文件").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/result?file=test.rar")

    # Click text=license for xlwt
    page.locator("text=license for xlwt").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/license?pack=xlwt")

    # Click text=开源供应链信息
    page.locator("text=开源供应链信息").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/result?file=None")

    # Go to http://202.121.180.97:30088/cve?pack=org
    page.goto("http://202.121.180.97:30088/cve?pack=org")

    # Go to http://202.121.180.97:30088/cves?file=None
    page.goto("http://202.121.180.97:30088/cves?file=None")

    # Click text=许可证信息
    page.locator("text=许可证信息").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/licenses?file=None")

    # Click text=合规性分析
    page.locator("text=合规性分析").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/legitimacy?file=None")

    # Click text=Home
    page.locator("text=Home").click()
    # expect(page).to_have_url("http://202.121.180.97:30088/")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
