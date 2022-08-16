from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://todomvc.com/examples/angular2/")
driver.maximize_window()
driver.implicitly_wait(5)
# new_todo = driver.find_element(By.XPATH, "/html/body/todo-app/section/header/input")
new_todo = driver.find_element(By.CLASS_NAME, "new-todo")
new_todo.send_keys("Hello, world!", Keys.ENTER)

# POSITIVE

# Test 1: user can add record
# 1. Open browser
# 2. Find input field
# 3. Input valid text
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 5. Assert: record is added


# Test 2: user can delete record
# 1. Open browser
# 2. Find input field
# 3. Input valid text
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 6. Press x to delete
# 5. Assert: record is deleted

# Test 3: user can mark the record as done
# 1. Open browser
# 2. Find input field
# 3. Input valid text
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 6. Press radiobutton to mark as done
# 5. Assert: record is marked as done

# Test 4: double click edits the record
# 1. Open browser
# 2. Find input field
# 3. Input valid text
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 6. Double click record
# 5. Assert: record is in editing mode

# Test 5: "Clear completed" appears
# 1. Open browser
# 2. Find input field
# 3. Input valid text
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 5. Assert: "Clear completed" appears

# Test 6: Counter changes
# 1. Open browser
# 2. Find input field
# 3. Input valid text
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 5. Assert: counter is changed

# NEGATIVE

# Test 1: Attempt submitting without text
# 1. Open browser
# 2. Find input field
# 3. Input no text
new_todo.send_keys("", Keys.ENTER)
# 4. Press enter
# 5. Assert: nothing happens, no new records

# Test 2: Attempt submitting long text
# 1. Open browser
# 2. Find input field
# 3. Input a lot of text
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 5. Assert: text is added

# Test 3: Special symbols (parametrize)
# 1. Open browser
# 2. Find input field
# 3. Input special symbols
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 5. Assert: text is added

# Test 4: Attempt submitting spaces
# 1. Open browser
# 2. Find input field
# 3. Input spaces
new_todo.send_keys("    ", Keys.ENTER)
# 4. Press enter
# 5. Assert: text isn't added

# Test 5: Attempt identical item entry
# 1. Open browser
# 2. Find input field
# 3. Input "check"
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 4. Press enter
# 5. Find input field
# 6. Input "check"
new_todo.send_keys("Hello, world!", Keys.ENTER)
# 7. Press enter
# 8. Assert: error for same data