import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class scheduler {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Take user input for the start date as calendar input
        System.out.println("Enter the start date (in the format YYYY MM DD): ");
        System.out.print("Year: ");
        int startYear = scanner.nextInt();
        System.out.print("Month (1-12): ");
        int startMonth = scanner.nextInt() - 1; // Calendar months are zero-based
        System.out.print("Day of the month: ");
        int startDay = scanner.nextInt();

        // Create a calendar instance with user input
        Calendar startDate = new GregorianCalendar(startYear, startMonth, startDay);

        // Ask how many days of schedule the user wants
        System.out.print("Enter number of days to generate schedule: ");
        int daysToGenerate = scanner.nextInt();

        // Iterate over the number of days and generate the schedule
        for (int i = 0; i < daysToGenerate; i++) {
            // Get the current date details
            int dayOfMonth = startDate.get(Calendar.DAY_OF_MONTH);
            int month = startDate.get(Calendar.MONTH) + 1; // Calendar.MONTH is zero-based
            int year = startDate.get(Calendar.YEAR);

            // Determine if it's WFH or WFO based on the date
            String schedule = getWFHOrWFOSchedule(startDate);

            // Print the schedule for the current day
            System.out.printf("%d-%02d-%02d: %s\n", year, month, dayOfMonth, schedule);

            // Move to the next day
            startDate.add(Calendar.DAY_OF_MONTH, 1);
        }

        scanner.close();
    }

    // Function to determine WFH or WFO schedule based on the date
    private static String getWFHOrWFOSchedule(Calendar calendar) {
        // The reference start date for the WFH/WFO pattern: September 19, 2024
        Calendar referenceDate = new GregorianCalendar(2024, Calendar.SEPTEMBER, 19);

        // Calculate the difference in days between the given date and the reference date
        long diffDays = (calendar.getTimeInMillis() - referenceDate.getTimeInMillis()) / (1000 * 60 * 60 * 24);

        // Apply the WFH/WFO pattern: 8-day rotation
        if ((diffDays / 8) % 2 == 0) {
            return "WFH"; // Work From Home
        } else {
            return "WFO"; // Work From Office
        }
    }
}
