from playwright.sync_api import sync_playwright


def run_test():
    with sync_playwright() as p:
        # Step 1: Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=True to run in the background
        page = browser.new_page()

        try:
            # Step 2: Navigate to eBay
            page.goto("https://www.ebay.com")

            # Step 3: Search for 'book'
            search_box = page.locator("input#gh-ac")
            search_box.fill("book")
            search_box.press("Enter")

            # Wait for search results to load
            page.wait_for_selector("li.s-item")
            page.pause()


            # Step 4: Click on the first book in the list
            # first_book = page.locator("(//li[contains(@class=s-item s-item__pl-on-bottom)])[1]")
            with page.expect_popup() as page1_info:
                first_book = page.locator("//li[@id='item5e661cbd1f']")

                first_book.click()
                # with page.expect_popup() as page1_info:
                #     page.get_by_alt_text("ISAAC J. STONES Isaac J").click()

            # page1 = page1_info.value
            # page1.get_by_test_id("x-atc-action").get_by_test_id("ux-call-to-action").click()
            # page1.goto("https://cart.payments.ebay.com/")
            # Wait for the item listing page to load
            page.wait_for_selector("button#atcRedesignId_btn")

            # Step 5: Click on 'Add to cart'
            add_to_cart_button = page.locator("button#atcRedesignId_btn")
            add_to_cart_button.click()

            # Wait for the cart to update
            page.wait_for_selector("a#gh-cart-i")

            # Step 6: Verify the cart has been updated
            cart_button = page.locator("a#gh-cart-i")
            cart_button.click()

            # Wait for the cart page to load
            page.wait_for_selector(".cart-bucket")

            # Check if the cart has at least one item
            cart_items = page.locator(".cart-bucket")
            if cart_items.count() > 0:
                print("Test Passed: Item successfully added to the cart.")
            else:
                print("Test Failed: Cart is empty.")

        finally:
            # Close the browser
            browser.close()


if __name__ == "__main__":
    run_test()
