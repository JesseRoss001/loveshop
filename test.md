# Testing

Return back to the [README.md](README.md) file.

## Manual Testing 

| Feature | Test Case| Outcome |
|-----------------|-----------------|-----------------|
| **Navbar:** | 
| Navbar: Hover| Hover over link on navbar | Pink border appears over hovered link. |
| Navbar: Home | Click on "Home" on each page | User successfully taken to home page. |
| Navbar: Products | Click on "Products" on each page | User successfully taken to Products page.  |
| Navbar: Products | Click on "Contact" on each page | User successfully taken to Contact page.  |
| Navbar: About us | Click on "About us" on each page | User successfully taken to About us page.  |
| Navbar: Login | Click on "Login" on each page | User successfully taken to Login page.  |
| Navbar: Register | Click on "Register" on each page | User successfully taken to Register page.  |
| **Animated Banner** | 
| Info Banner | Display info about delivery | The animated banner alternately displays information about free shipping in the UK and the final order deadline for next-day delivery.  |
| **Homepage** | 
| "shop Now" button | Click the button | User successfully taken to Products page.  |
| Homepage content | Display page content | Welcome text and the animation are displayed and fully responsive.  |
| **Products page** | 
| Shopping Cart | Only logged in user is able to access the shopping cart | Cart is not clickable for not logged in users.  |
| Shopping Cart empty | Click on an empty shopping cart  | Empty cart info displayed. |
| Shopping Cart full | Click on a full shopping cart button | Displays list of products in the cart. |
| Remove item from shopping cart | Click on remove button | Removes item from cart and updates the cart list. |
| Continue shopping button | Click on the Continue Shopping button | Redirects to the products page. |
| Go to checkout button | Click on the Go to checkout button | Directs user to the checkout page. |
| Filter | Filter search criteria | Clicking on the filter button successfully filters the viewed products.  |
| "Valentine's special section | Display Valentine's special products | Display three products from Valentine's special offer.  |
| Expand the "Valentine's special section | Click on the "Show more" button | Display the rest of the Valentine's special products.  |
| Fold the "Valentine's special section | Click on the "Show less" button | Folds the section just to three products.  |
| Add to cart button | Click on the button | Clicking the button adds the item to the shopping cart (the button is visible only for logged-in users).  |
| "Info" button | clickable button | Clicking the button on each product opens a modal with product description.  |
| Pagination | Change the product page button | Clicking on the "Next", "Last", "First" and "Previous" button changes the product page.  |
| **Contact page** | 
| Signup form | Submit a form | All fields are required. After filling all fields, Submit button redirect user to the Thank you page. |
| FAQ Accordion | Click a question to display answer | Answer cards successfully expand and collapse.  |
| **About Us page** | 
| Page content | Display page content | About Us content and animation are displayed and fully responsive. |
| **Register page** | 
| Register form | Fill the form to register | All fields are required. The email and phone number must have valid format to proceed. Both passwords must match to complete the registration. After filling in all the correct data, the user is registered and redirected to the home page. |
| **Login page** | 
| Login form | Fill the form to login | Only already registered users will be able to log in. Failing to provide the correct login or password will result in the page being reloaded to the login form again.  |
| **Logout** | 
| Logout button | Logout the user | Button visible only for logged in user, clicking on the log out button logs out the user and reload the page.  |
| **Footer** | 
| Email address| Click on the email address | Clicking on email address successfully opens email window.  |
| Phone number| Click on the phone number | Clicking on the phone number successfully opens a modal window to connect through FaceTime.  |
| Social media links| Click on a social media icon | Clicking the icon successfully opens a new tab linking to the relevant social media page.  |
| Copyrights info | Display copyrights informaton | Display the name of the site owner along with the current year.  |
| **Checkout Page** | 
| Checkout form | Fill the checkout form | Fill all fields to proceed to payment  |
| Proceed to payment button | Click on the payment button | Clicking on the Proceed to payment button directs to the Review order page.  |
| **Review Order Page** | 
| Review Order list | Display ordered product list | Displays all ordered products with the names and prices. |
| Proceed to payment button | Click on the payment button | Clicking on the Proceed to payment button directs to the secure Stripe payment page.  |
| Shop more button | Click on the shop more button | Clicking on the Shop moret button directs back to the product page.  |
| **Secure Stripe Payment Page** |
| Back button | Click on the Back button | Clicking on the Back button directs to the Cancelled payment page.  |
| Order Info | Displays order information | Displays the amount to pay, and products name with prices with quantity.  |
| Stripe form | Fill the payment form | All fields required to proceed payment. |
| Pay button | Click on the Pay button | With the form being filled correctly clicking on the Pay button will directs to the Payment Successful page.  |
| **Payment Successful Page** |
| Successful payment page | Displays Info about successful payment |  Displays Info and animation about successful payment. |
| **Payment Cancelled Page** |
| Payment Cancelled page | Displays Info about cancelled payment |  Displays Info and animation about cancelled payment. |

### Browser Compatibility:
| Browser Tested       | Intended appearance          | intended Responsiveness  |
| ------------- |:-------------:| -----:|
| Chrome      | Good | Good |
| Mozilla      | Good      |   Good |
| Safari | Good      |    Good |
| Edge | Good      |    Good |

### Responsiveness Test:
| Device Tested | Site Responsiveness >700px | Site Responsiveness <699px | Renders as Expected |
| ------------- | --------------------------- | --------------------------- | ------------------- |
| iPhone Pro     |N/A                | Responsive                 | Yes                 |
| iPhone 11      |N/A                | Responsive                 | Yes                 |
| Samsung Galaxy S8      |N/A                | Responsive                 | Yes                 |
| Desktop 1024px | Responsive                 | N/A                 | Yes                 |

## Bugs and Issues

| # | Bugs, Errors and Issues | Description |
| :--- | :--- | :--- |
| 1 | Checkout button works on empty shopping cart | It is possible to go to checkout page with an empty bag. |
| 2 | Checkout form required field | On the checkout form only the postal code is required, so user can proceed to payment without full address. |

Due to time constraints, we were unable to address all of the bugs found during the testing process.

## Conclusion

Based on the testing conducted on the website, the following conclusions can be drawn:

1. **Navbar Functionality**: The navbar elements were tested for their responsiveness and functionality across different pages. Users were successfully navigated to the intended pages upon clicking each navbar item.

2. **Homepage and Products Page**: Key features like the "Shop Now" button and product filtering were tested on the homepage and products page respectively. Users were successfully redirected to the Products page upon clicking the "Shop Now" button, and the filtering functionality worked as expected.

3. **Contact Page and Footer**: Testing on the contact page focused on form submission and FAQ accordion functionality, both of which were successfully implemented. In addition, interactions with the footer elements such as email addresses and social media links were smooth and responsive.

4. **Browser Compatibility**: The website exhibited good appearance and responsiveness across popular browsers including Chrome, Mozilla, Safari, and Edge, ensuring a consistent user experience regardless of the browser used.

5. **Responsiveness Across Devices**: The website was tested for responsiveness on various devices including iPhones, Samsung Galaxy, and desktops. It displayed intended responsiveness and rendered as expected across different screen sizes, ensuring accessibility across a wide range of devices.

In conclusion, the testing demonstrated that the website performs well across various functionalities, browsers, and devices. The identified features and elements behaved as intended, providing users with a seamless and reliable experience. However, it's crucial to continue monitoring and testing regularly to maintain optimal performance and user satisfaction.

