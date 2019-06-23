1. Setup a virtual environment.
2. Fork the repository for [Django REST Task 2](https://github.com/JoinCODED/REST_task_01/) in JoinCODED’s Github and Clone it.
3. Install the packages from the requirements file.
4. Create an API detail view:
    * which will display the following fields for the `Booking` object:
      * `id`
      * `flight`
      * `date`
      * `passengers`
    * Create a `URL` for this view and test it in `postman`.
    * Replace the api in the **frontends** `booking_details` view with this api.
5. Create an API update view:
    * which will allow you to edit the following fields for the `Booking` object:
      * `passengers`
      * `date`
    * Create a `URL` for this view and test it in `postman`.
    * Replace the api in the **frontends** `modify_booking` view with this api.
6. Create an API delete view to cancel a `Booking`.
    * Create a `URL` for this view and test it in `postman`.
    * Replace the api in the **frontends** `cancel_booking` view with this api.
7. Push your code
