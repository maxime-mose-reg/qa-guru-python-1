from selene import have
from selene.support.conditions.have import text
from selene.support.shared import browser

browser.open('https://demoqa.com/automation-practice-form')
browser.element('h5').should(have.text('Student Registration Form'))

browser.element('#firstName').type('Ivan')
browser.element('#lastName').type('Ivanov')
browser.element('#userEmail').type('ivanov@mail.ru')
browser.element('[value=Male]').parent_element.click()
browser.element('#userNumber').type('9151001010')

browser.element('#dateOfBirthInput').click()
browser.element('option[value="1999"]').click()
browser.elements('.react-datepicker__month-select option').element_by(text('December')).click()
browser.element('.react-datepicker__day--031:not(.react-datepicker__day--outside-month)').click()

browser.element('#subjectsInput').type('Maths').press_enter()
browser.elements('[for^=hobbies-checkbox]').element_by(text('Sports')).click()
# TODO browser.elements('#uploadPicture')
browser.element('#currentAddress').type('Current Address')
browser.element('#state input').scroll_to().type('NCR').press_enter()
browser.element('#city input').type('Delhi').press_enter().press_enter()

browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
elements = browser.elements('td')
elements.element_by(text('Student Name')).following_sibling.should(have.text('Ivan Ivanov'))
elements.element_by(text('Student Email')).following_sibling.should(have.text('ivanov@mail.ru'))
elements.element_by(text('Gender')).following_sibling.should(have.text('Male'))
elements.element_by(text('Mobile')).following_sibling.should(have.text('9151001010'))
elements.element_by(text('Date of Birth')).following_sibling.should(have.text('31 December,1999'))
elements.element_by(text('Subjects')).following_sibling.should(have.text('Maths'))
elements.element_by(text('Hobbies')).following_sibling.should(have.text('Sports'))
# TODO elements.element_by(text('Picture')).following_sibling.should(have.text('pic.png'))
elements.element_by(text('Address')).following_sibling.should(have.text('Current Address'))
elements.element_by(text('State and City')).following_sibling.should(have.text('NCR Delhi'))
