from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()


def run_chrome():
    webdriver.Chrome()
    driver.get("https://todomvc.com/examples/angular2/")
    driver.implicitly_wait(5)


def enter_todo(test_text):
    new_todo = driver.find_element(By.CLASS_NAME, "new-todo")
    new_todo.send_keys(test_text)
    new_todo.send_keys(Keys.ENTER)
    print("Todo \'" + test_text + "\' was added!")


# POSITIVE

# Test 1: user can add record
print("Test 1: user can add record")
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input valid text
# 4. Press enter
enter_todo("Buy some bread and cheese")
# 5. Check if record is added
if driver.find_elements(By.XPATH, "/html/body/todo-app/section/section/ul/li/div/label"):
    print("Test 1 PASSED, todo was added.")
else:
    print("Test 1 FAILED, todo wasn't added.")
# 6. Close browser.

# Test 2: user can delete record
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input valid text
# 4. Press enter
enter_todo("Buy some milk")


# 5. Find x

def click_delete():
    todo_item = driver.find_element(By.XPATH, "//todo-app//li[last()]")
    hover = ActionChains(driver).move_to_element(todo_item)
    hover.perform()
    delete_button = driver.find_element(By.CLASS_NAME, "destroy")
    hover = ActionChains(driver).move_to_element(delete_button)
    hover.perform()
    delete_button.click()


click_delete()

# 6. Press x to delete

# 5. Assert: record is deleted
if not driver.find_elements(By.XPATH, "//todo-app//li[last()]"):
    print("Test 2 PASSED, todo was deleted.")
else:
    print("Test 2 FAILED, todo wasn't deleted.")

# Test 3: user can mark the record as done
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input valid text
# 4. Press enter
enter_todo("Wake up early")


# 6. Press radiobutton to mark as done
def mark_done(xpath):
    toggle_item = driver.find_element(By.XPATH, xpath)
    toggle_item.click()

mark_done("//todo-app//li[last()]/div/input")

# 5. Assert: record is marked as done

if driver.find_elements(By.CLASS_NAME, "completed"):
    print("Test 3 PASSED, item was marked as done.")
else:
    print("Test 3 FAILED, item was not marked as done.")

# Test 4: double click edits the record
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input valid text
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 6. Double click record
# 5. Assert: record is in editing mode

# Test 5: "Clear completed" appears
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input valid text
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 5. Assert: "Clear completed" appears

# Test 6: Counter changes
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input valid text
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 5. Assert: counter is changed

# NEGATIVE

# Test 1: Attempt submitting without text
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input no text
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 5. Assert: nothing happens, no new records

# Test 2: Attempt submitting long text
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input a lot of text
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 5. Assert: text is added

# Test 3: Special symbols (parametrize)
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input special symbols
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 5. Assert: text is added

# Test 4: Attempt submitting spaces
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input spaces
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 5. Assert: text isn't added

# Test 5: Attempt identical item entry
# 1. Open browser
run_chrome()
# 2. Find input field
# 3. Input "check"
enter_todo("Buy some bread and cheese")
# 4. Press enter
# 5. Find input field
# 6. Input "check"
enter_todo("Buy some bread and cheese")
# 7. Press enter
# 8. Assert: error for same data

# driver.close()
