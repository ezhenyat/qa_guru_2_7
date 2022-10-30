from demoqa_tests.model import app


def test_submit_student_registration_form():
    app.registration_form.given_opened()

    # WHEN
    app.registration_form.set_name('Аркадий')
    app.registration_form.set_last_name('Светов')
    app.registration_form.set_email('mrlibertarian@gmail.com')
    app.registration_form.set_gender('Male')
    app.registration_form.set_phone_number('5990807420')
    app.registration_form.set_date_of_birth('29 Dec 1996')
    app.registration_form.set_subjects('Maths', 'Biology')
    app.registration_form.set_hobbies('Reading', 'Sports')
    app.registration_form.picture_upload('test_media/kitten.png')
    app.registration_form.set_address('Petre Kavtaradze 19')
    app.registration_form.scroll_to_bottom()
    app.registration_form.set_state('NCR')
    app.registration_form.set_city('Delhi')

    app.registration_form.submit()

    # THEN

    app.registration_form.should_have_submitted(
        [
            ('Student Name', 'Аркадий Светов'),
            ('Student Email', 'mrlibertarian@gmail.com'),
            ('Mobile', '5990807420'),
            ('Date of Birth', '30 October,2022'),
            ('Subjects', 'Maths, Biology'),
            ('Hobbies', 'Reading, Sports'),
            ('Picture', 'kitten.png'),
            ('Address', 'Petre Kavtaradze 19'),
            ('State', 'NCR Delhi'),
        ],
    )