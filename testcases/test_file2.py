from POM.AbhiBus import AbhiBus

def test_select_bus(setup):

    context = setup.new_context(no_viewport=True)

    try:
        page = context.new_page()

        abhi_bus = AbhiBus(page)

        abhi_bus.book_buses("Bengaluru","Hyderabad")

    finally:
        context.close()