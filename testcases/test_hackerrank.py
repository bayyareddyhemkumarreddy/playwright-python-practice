from playwright.sync_api import expect

from POM.hackerrank_home_page import HackerRankHomePage


class TestHackerRank:

    def test_home_page_title(self,setup):
        context=setup.new_context(no_viewport=True)
        page=context.new_page()
        page = HackerRankHomePage(page)
        title=page.get_home_page_title()
        expect(title).to_have_title("HackerRank - Online Coding Tests and Technical Interviews")
        page.scroll_to_element()
        page.play_video()
        page.close_video()
        page.select_product()

