// Uncomment each of the following lines after you have completed the corresponding tasks
// Tip: Use Ctrl/Cmd + / on VS Code

#define TASK1_UTILITY_COMPLETE
#define TASK2_BOARD_COMPLETE
#define TASK3_1_LEAPER_COMPLETE
#define TASK3_2_RIDER_COMPLETE
#define TASK3_3_COMPOUND_COMPLETE
#define TASK3_4_DIVERGENT_COMPLETE
#define TASK4_1_2_PIECES_COMPLETE
#define TASK4_3_PAWN_COMPLETE
#define TASK5_BOARD_FUNC_COMPLETE


// Do not modify anything below this line
// They give warnings or errors if you complete tasks out of order
#if (defined(TASK3_1_LEAPER_COMPLETE) | defined(TASK3_2_RIDER_COMPLETE)) & !defined(TASK2_BOARD_COMPLETE)
    #warning "Task 3 may not function properly if Task 2 is not completed."
#endif

#if defined(TASK3_3_COMPOUND_COMPLETE) & !defined(TASK3_1_LEAPER_COMPLETE) & !defined(TASK3_2_RIDER_COMPLETE)
    #error "You should complete Leaper and Rider before testing Compound!"
#endif

#if defined(TASK3_4_DIVERGENT_COMPLETE) & !defined(TASK3_1_LEAPER_COMPLETE) & !defined(TASK3_2_RIDER_COMPLETE)
    #error "You should complete Leaper and Rider before testing Divergent!"
#endif

#if defined(TASK5_BOARD_FUNC_COMPLETE) & !defined(TASK4_1_2_PIECES_COMPLETE) & !defined(TASK4_3_PAWN_COMPLETE)
    #error "You should complete Task 4 before testing Task 5!"
#endif
