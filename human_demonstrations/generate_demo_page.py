import jinja2
from google.cloud import storage

demos = [
    "assembling_gift_baskets_0_Beechwood_0_int_2021-05-28_13-32-07_episode.hdf5",
    "assembling_gift_baskets_0_Beechwood_0_int_2021-05-30_14-30-15_episode.hdf5",
    "assembling_gift_baskets_0_Beechwood_0_int_2021-06-01_14-11-09_episode.hdf5",
    "assembling_gift_baskets_0_Beechwood_0_int_2021-06-22_14-34-09_episode.hdf5",
    "assembling_gift_baskets_0_Pomaria_1_int_2021-06-04_18-30-20_episode.hdf5",
    "bottling_fruit_0_Benevolence_1_int_2021-05-24_22-33-41_episode.hdf5",
    "bottling_fruit_0_Wainscott_0_int_2021-05-24_19-46-46_episode.hdf5",
    "bottling_fruit_0_Wainscott_0_int_2021-05-30_14-38-11_episode.hdf5",
    "bottling_fruit_0_Wainscott_0_int_2021-06-05_18-37-24_episode.hdf5",
    "bottling_fruit_0_Wainscott_0_int_2021-06-22_14-43-48_episode.hdf5",
    "boxing_books_up_for_storage_0_Benevolence_1_int_2021-05-27_18-47-09_episode.hdf5",
    "boxing_books_up_for_storage_0_Benevolence_1_int_2021-06-01_14-17-46_episode.hdf5",
    "boxing_books_up_for_storage_0_Benevolence_1_int_2021-06-05_19-24-23_episode.hdf5",
    "boxing_books_up_for_storage_0_Benevolence_1_int_2021-06-22_14-53-13_episode.hdf5",
    "boxing_books_up_for_storage_0_Merom_0_int_2021-05-24_17-46-04_episode.hdf5",
    "bringing_in_wood_0_Benevolence_1_int_2021-05-28_13-58-41_episode.hdf5",
    "bringing_in_wood_0_Benevolence_1_int_2021-05-30_15-36-02_episode.hdf5",
    "bringing_in_wood_0_Benevolence_1_int_2021-06-01_14-31-43_episode.hdf5",
    "bringing_in_wood_0_Pomaria_1_int_2021-06-04_18-36-25_episode.hdf5",
    "brushing_lint_off_clothing_0_Benevolence_2_int_2021-06-04_18-40-06_episode.hdf5",
    "brushing_lint_off_clothing_0_Pomaria_2_int_2021-06-02_16-02-55_episode.hdf5",
    "brushing_lint_off_clothing_0_Pomaria_2_int_2021-06-04_16-14-19_episode.hdf5",
    "brushing_lint_off_clothing_0_Pomaria_2_int_2021-06-04_17-41-56_episode.hdf5",
    "brushing_lint_off_clothing_0_Pomaria_2_int_2021-06-22_15-02-21_episode.hdf5",
    "chopping_vegetables_0_Rs_int_2021-05-25_22-01-16_episode.hdf5",
    "chopping_vegetables_0_Rs_int_2021-05-30_15-25-12_episode.hdf5",
    "chopping_vegetables_0_Rs_int_2021-06-03_12-33-18_episode.hdf5",
    "chopping_vegetables_0_Rs_int_2021-06-22_15-09-10_episode.hdf5",
    "chopping_vegetables_0_Wainscott_0_int_2021-06-06_17-43-07_episode.hdf5",
    "cleaning_a_car_0_Ihlen_0_int_2021-05-22_20-20-20_episode.hdf5",
    "cleaning_a_car_0_Ihlen_0_int_2021-05-25_19-33-34_episode.hdf5",
    "cleaning_a_car_0_Ihlen_0_int_2021-05-30_15-04-53_episode.hdf5",
    "cleaning_a_car_0_Ihlen_0_int_2021-06-12_19-27-35_episode.hdf5",
    "cleaning_barbecue_grill_0_Ihlen_0_int_2021-05-27_19-03-38_episode.hdf5",
    "cleaning_barbecue_grill_0_Ihlen_0_int_2021-05-30_15-09-21_episode.hdf5",
    "cleaning_barbecue_grill_0_Ihlen_0_int_2021-06-01_14-46-44_episode.hdf5",
    "cleaning_barbecue_grill_0_Ihlen_0_int_2021-06-12_19-31-04_episode.hdf5",
    "cleaning_bathrooms_0_Benevolence_0_int_2021-05-23_16-33-46_episode.hdf5",
    "cleaning_bathrooms_0_Benevolence_0_int_2021-06-02_16-08-34_episode.hdf5",
    "cleaning_bathrooms_0_Benevolence_0_int_2021-06-03_13-04-11_episode.hdf5",
    "cleaning_bathrooms_0_Benevolence_0_int_2021-06-12_19-33-28_episode.hdf5",
    "cleaning_bathrooms_0_Merom_1_int_2021-06-10_21-00-27_episode.hdf5",
    "cleaning_bathtub_0_Benevolence_0_int_2021-05-22_17-09-37_episode.hdf5",
    "cleaning_bathtub_0_Benevolence_0_int_2021-05-22_17-15-40_episode.hdf5",
    "cleaning_bathtub_0_Pomaria_0_int_2021-05-22_17-35-47_episode.hdf5",
    "cleaning_bathtub_0_Pomaria_0_int_2021-05-22_17-39-57_episode.hdf5",
    "cleaning_bathtub_0_Pomaria_0_int_2021-05-30_15-40-42_episode.hdf5",
    "cleaning_bathtub_0_Pomaria_0_int_2021-06-12_19-36-51_episode.hdf5",
    "cleaning_bedroom_0_Beechwood_1_int_2021-05-27_11-44-41_episode.hdf5",
    "cleaning_bedroom_0_Beechwood_1_int_2021-06-02_16-17-17_episode.hdf5",
    "cleaning_bedroom_0_Beechwood_1_int_2021-06-03_13-11-29_episode.hdf5",
    "cleaning_bedroom_0_Beechwood_1_int_2021-06-12_19-40-30_episode.hdf5",
    "cleaning_bedroom_0_Benevolence_2_int_2021-06-06_18-10-59_episode.hdf5",
    "cleaning_carpets_0_Beechwood_0_int_2021-06-06_18-17-02_episode.hdf5",
    "cleaning_carpets_0_Wainscott_1_int_2021-05-28_17-10-20_episode.hdf5",
    "cleaning_carpets_0_Wainscott_1_int_2021-06-02_16-36-44_episode.hdf5",
    "cleaning_carpets_0_Wainscott_1_int_2021-06-03_13-47-16_episode.hdf5",
    "cleaning_carpets_0_Wainscott_1_int_2021-06-23_15-55-58_episode.hdf5",
    "cleaning_closet_0_Beechwood_1_int_2021-05-28_17-56-08_episode.hdf5",
    "cleaning_closet_0_Beechwood_1_int_2021-06-02_16-49-56_episode.hdf5",
    "cleaning_closet_0_Beechwood_1_int_2021-06-03_13-20-44_episode.hdf5",
    "cleaning_closet_0_Beechwood_1_int_2021-06-11_19-57-59_episode.hdf5",
    "cleaning_cupboards_0_Merom_1_int_2021-06-06_18-22-23_episode.hdf5",
    "cleaning_cupboards_0_Wainscott_1_int_2021-05-28_18-23-50_episode.hdf5",
    "cleaning_cupboards_0_Wainscott_1_int_2021-06-02_21-54-33_episode.hdf5",
    "cleaning_cupboards_0_Wainscott_1_int_2021-06-03_13-54-06_episode.hdf5",
    "cleaning_floors_0_Merom_0_int_2021-05-23_22-21-35_episode.hdf5",
    "cleaning_floors_0_Merom_0_int_2021-06-02_17-12-18_episode.hdf5",
    "cleaning_floors_0_Merom_0_int_2021-06-03_14-06-34_episode.hdf5",
    "cleaning_floors_0_Merom_0_int_2021-06-23_16-12-28_episode.hdf5",
    "cleaning_floors_0_Pomaria_0_int_2021-06-06_18-28-10_episode.hdf5",
    "cleaning_freezer_0_Pomaria_1_int_2021-05-28_18-31-16_episode.hdf5",
    "cleaning_freezer_0_Pomaria_1_int_2021-06-02_17-16-44_episode.hdf5",
    "cleaning_freezer_0_Pomaria_1_int_2021-06-03_14-10-22_episode.hdf5",
    "cleaning_freezer_0_Pomaria_1_int_2021-06-23_16-16-37_episode.hdf5",
    "cleaning_freezer_0_Wainscott_0_int_2021-06-06_18-35-14_episode.hdf5",
    "cleaning_garage_0_Ihlen_0_int_2021-05-23_19-08-05_episode.hdf5",
    "cleaning_garage_0_Ihlen_0_int_2021-06-02_17-20-36_episode.hdf5",
    "cleaning_garage_0_Ihlen_0_int_2021-06-03_15-47-13_episode.hdf5",
    "cleaning_garage_0_Ihlen_0_int_2021-06-23_16-20-00_episode.hdf5",
    "cleaning_high_chair_0_Merom_1_int_2021-05-23_23-26-19_episode.hdf5",
    "cleaning_high_chair_0_Wainscott_0_int_2021-05-23_23-22-28_episode.hdf5",
    "cleaning_high_chair_0_Wainscott_0_int_2021-06-01_16-13-20_episode.hdf5",
    "cleaning_high_chair_0_Wainscott_0_int_2021-06-05_18-03-15_episode.hdf5",
    "cleaning_high_chair_0_Wainscott_0_int_2021-06-23_16-28-09_episode.hdf5",
    "cleaning_kitchen_cupboard_0_Pomaria_1_int_2021-05-24_11-37-02_episode.hdf5",
    "cleaning_kitchen_cupboard_0_Pomaria_1_int_2021-06-02_17-47-41_episode.hdf5",
    "cleaning_kitchen_cupboard_0_Pomaria_1_int_2021-06-06_17-09-54_episode.hdf5",
    "cleaning_kitchen_cupboard_0_Pomaria_1_int_2021-06-23_16-35-04_episode.hdf5",
    "cleaning_kitchen_cupboard_0_Wainscott_0_int_2021-06-08_16-10-02_episode.hdf5",
    "cleaning_microwave_oven_0_Benevolence_1_int_2021-05-23_17-06-26_episode.hdf5",
    "cleaning_microwave_oven_0_Benevolence_1_int_2021-05-31_11-57-51_episode.hdf5",
    "cleaning_microwave_oven_0_Benevolence_1_int_2021-06-01_14-51-24_episode.hdf5",
    "cleaning_microwave_oven_0_Benevolence_1_int_2021-06-23_16-44-10_episode.hdf5",
    "cleaning_microwave_oven_0_Rs_int_2021-06-06_18-52-15_episode.hdf5",
    "cleaning_out_drawers_0_Benevolence_1_int_2021-05-23_17-16-19_episode.hdf5",
    "cleaning_out_drawers_0_Benevolence_1_int_2021-06-02_18-46-47_episode.hdf5",
    "cleaning_out_drawers_0_Benevolence_1_int_2021-06-03_15-53-37_episode.hdf5",
    "cleaning_out_drawers_0_Benevolence_1_int_2021-06-23_16-47-46_episode.hdf5",
    "cleaning_out_drawers_0_Rs_int_2021-06-08_16-31-47_episode.hdf5",
    "cleaning_oven_0_Benevolence_1_int_2021-05-23_17-33-26_episode.hdf5",
    "cleaning_oven_0_Benevolence_1_int_2021-05-31_12-06-52_episode.hdf5",
    "cleaning_oven_0_Benevolence_1_int_2021-06-01_14-55-38_episode.hdf5",
    "cleaning_oven_0_Rs_int_2021-06-06_19-15-39_episode.hdf5",
    "cleaning_shoes_0_Benevolence_2_int_2021-06-06_19-20-58_episode.hdf5",
    "cleaning_shoes_0_Pomaria_2_int_2021-05-27_18-36-09_episode.hdf5",
    "cleaning_shoes_0_Pomaria_2_int_2021-05-31_12-14-06_episode.hdf5",
    "cleaning_shoes_0_Pomaria_2_int_2021-06-01_14-59-50_episode.hdf5",
    "cleaning_shoes_0_Pomaria_2_int_2021-06-23_17-02-26_episode.hdf5",
    "cleaning_sneakers_0_Pomaria_1_int_2021-05-28_18-36-07_episode.hdf5",
    "cleaning_sneakers_0_Pomaria_1_int_2021-05-31_12-21-20_episode.hdf5",
    "cleaning_sneakers_0_Pomaria_1_int_2021-06-01_15-04-59_episode.hdf5",
    "cleaning_stove_0_Merom_1_int_2021-06-08_16-37-49_episode.hdf5",
    "cleaning_stove_0_Wainscott_0_int_2021-05-30_12-41-55_episode.hdf5",
    "cleaning_stove_0_Wainscott_0_int_2021-05-31_12-30-44_episode.hdf5",
    "cleaning_stove_0_Wainscott_0_int_2021-06-01_15-16-01_episode.hdf5",
    "cleaning_stove_0_Wainscott_0_int_2021-06-23_17-18-20_episode.hdf5",
    "cleaning_table_after_clearing_0_Beechwood_0_int_2021-05-22_21-29-48_episode.hdf5",
    "cleaning_table_after_clearing_0_Beechwood_0_int_2021-05-30_16-22-52_episode.hdf5",
    "cleaning_table_after_clearing_0_Beechwood_0_int_2021-06-01_15-22-45_episode.hdf5",
    "cleaning_table_after_clearing_0_Beechwood_0_int_2021-06-23_17-23-43_episode.hdf5",
    "cleaning_table_after_clearing_0_Merom_1_int_2021-06-06_19-48-44_episode.hdf5",
    "cleaning_the_hot_tub_0_Ihlen_0_int_2021-05-27_19-25-29_episode.hdf5",
    "cleaning_the_hot_tub_0_Ihlen_0_int_2021-05-30_16-29-46_episode.hdf5",
    "cleaning_the_hot_tub_0_Ihlen_0_int_2021-06-01_15-27-17_episode.hdf5",
    "cleaning_the_hot_tub_0_Ihlen_0_int_2021-06-23_17-27-49_episode.hdf5",
    "cleaning_the_pool_0_Ihlen_0_int_2021-05-28_18-45-06_episode.hdf5",
    "cleaning_the_pool_0_Ihlen_0_int_2021-05-30_16-33-37_episode.hdf5",
    "cleaning_the_pool_0_Ihlen_0_int_2021-06-01_15-30-31_episode.hdf5",
    "cleaning_the_pool_0_Ihlen_0_int_2021-06-23_17-31-12_episode.hdf5",
    "cleaning_toilet_0_Benevolence_2_int_2021-06-06_19-51-44_episode.hdf5",
    "cleaning_toilet_0_Merom_0_int_2021-05-27_18-08-44_episode.hdf5",
    "cleaning_toilet_0_Merom_0_int_2021-05-31_12-36-33_episode.hdf5",
    "cleaning_toilet_0_Merom_0_int_2021-06-01_15-36-47_episode.hdf5",
    "cleaning_toilet_0_Merom_0_int_2021-06-23_17-35-48_episode.hdf5",
    "cleaning_up_after_a_meal_0_Merom_1_int_2021-06-06_19-55-27_episode.hdf5",
    "cleaning_up_after_a_meal_0_Wainscott_0_int_2021-05-27_18-01-14_episode.hdf5",
    "cleaning_up_after_a_meal_0_Wainscott_0_int_2021-05-31_12-47-49_episode.hdf5",
    "cleaning_up_after_a_meal_0_Wainscott_0_int_2021-06-01_15-41-54_episode.hdf5",
    "cleaning_up_refrigerator_0_Pomaria_1_int_2021-06-06_20-03-49_episode.hdf5",
    "cleaning_up_refrigerator_0_Wainscott_0_int_2021-05-30_12-49-18_episode.hdf5",
    "cleaning_up_refrigerator_0_Wainscott_0_int_2021-05-31_12-57-46_episode.hdf5",
    "cleaning_up_refrigerator_0_Wainscott_0_int_2021-06-01_15-49-39_episode.hdf5",
    "cleaning_up_refrigerator_0_Wainscott_0_int_2021-06-23_17-46-01_episode.hdf5",
    "cleaning_up_the_kitchen_only_0_Pomaria_1_int_2021-05-24_18-40-25_episode.hdf5",
    "cleaning_up_the_kitchen_only_0_Pomaria_1_int_2021-05-31_13-03-21_episode.hdf5",
    "cleaning_up_the_kitchen_only_0_Pomaria_1_int_2021-06-01_15-55-41_episode.hdf5",
    "cleaning_windows_0_Rs_int_2021-05-23_23-11-46_episode.hdf5",
    "cleaning_windows_0_Wainscott_0_int_2021-05-23_23-07-05_episode.hdf5",
    "cleaning_windows_0_Wainscott_0_int_2021-06-04_16-57-09_episode.hdf5",
    "cleaning_windows_0_Wainscott_0_int_2021-06-05_17-54-40_episode.hdf5",
    "cleaning_windows_0_Wainscott_0_int_2021-06-16_18-24-10_episode.hdf5",
    "cleaning_windows_0_Wainscott_0_int_2021-06-23_17-52-10_episode.hdf5",
    "clearing_the_table_after_dinner_0_Beechwood_0_int_2021-05-22_21-20-08_episode.hdf5",
    "clearing_the_table_after_dinner_0_Benevolence_1_int_2021-05-23_17-44-35_episode.hdf5",
    "clearing_the_table_after_dinner_0_Ihlen_0_int_2021-05-23_19-40-56_episode.hdf5",
    "clearing_the_table_after_dinner_0_Ihlen_0_int_2021-06-04_17-06-49_episode.hdf5",
    "clearing_the_table_after_dinner_0_Ihlen_0_int_2021-06-05_18-49-57_episode.hdf5",
    "clearing_the_table_after_dinner_0_Ihlen_0_int_2021-06-23_17-58-40_episode.hdf5",
    "collect_misplaced_items_0_Merom_1_int_2021-05-23_21-36-30_episode.hdf5",
    "collect_misplaced_items_0_Wainscott_0_int_2021-05-23_21-43-26_episode.hdf5",
    "collect_misplaced_items_0_Wainscott_0_int_2021-06-01_16-20-19_episode.hdf5",
    "collect_misplaced_items_0_Wainscott_0_int_2021-06-06_11-54-11_episode.hdf5",
    "collecting_aluminum_cans_0_Ihlen_1_int_2021-06-06_20-13-28_episode.hdf5",
    "collecting_aluminum_cans_0_Pomaria_2_int_2021-05-24_22-03-38_episode.hdf5",
    "collecting_aluminum_cans_0_Pomaria_2_int_2021-05-31_13-14-08_episode.hdf5",
    "collecting_aluminum_cans_0_Pomaria_2_int_2021-06-01_21-22-58_episode.hdf5",
    "collecting_aluminum_cans_0_Pomaria_2_int_2021-06-23_18-02-20_episode.hdf5",
    "defrosting_freezer_0_Beechwood_0_int_2021-05-28_19-06-26_episode.hdf5",
    "defrosting_freezer_0_Beechwood_0_int_2021-05-31_13-24-31_episode.hdf5",
    "defrosting_freezer_0_Beechwood_0_int_2021-06-01_21-29-25_episode.hdf5",
    "defrosting_freezer_0_Beechwood_0_int_2021-06-23_18-11-09_episode.hdf5",
    "defrosting_freezer_0_Ihlen_1_int_2021-06-06_20-17-31_episode.hdf5",
    "filling_a_Christmas_stocking_0_Beechwood_0_int_2021-06-07_14-08-23_episode.hdf5",
    "filling_a_Christmas_stocking_0_Rs_int_2021-05-25_22-46-38_episode.hdf5",
    "filling_a_Christmas_stocking_0_Rs_int_2021-05-31_13-38-39_episode.hdf5",
    "filling_a_Christmas_stocking_0_Rs_int_2021-06-04_18-47-42_episode.hdf5",
    "filling_an_Easter_basket_0_Benevolence_1_int_2021-05-28_19-50-04_episode.hdf5",
    "filling_an_Easter_basket_0_Benevolence_1_int_2021-05-31_13-48-23_episode.hdf5",
    "filling_an_Easter_basket_0_Benevolence_1_int_2021-06-02_20-54-35_episode.hdf5",
    "installing_a_fax_machine_0_Beechwood_0_int_2021-05-28_19-56-57_episode.hdf5",
    "installing_a_fax_machine_0_Beechwood_0_int_2021-05-31_13-59-32_episode.hdf5",
    "installing_a_fax_machine_0_Beechwood_0_int_2021-06-02_21-01-21_episode.hdf5",
    "installing_a_fax_machine_0_Beechwood_0_int_2021-06-12_19-06-54_episode.hdf5",
    "installing_a_fax_machine_0_Pomaria_0_int_2021-06-08_18-26-19_episode.hdf5",
    "installing_a_modem_0_Beechwood_0_int_2021-05-22_20-13-43_episode.hdf5",
    "installing_a_modem_0_Beechwood_0_int_2021-05-31_14-04-03_episode.hdf5",
    "installing_a_modem_0_Beechwood_0_int_2021-06-02_21-05-56_episode.hdf5",
    "installing_a_modem_0_Beechwood_0_int_2021-06-12_19-11-16_episode.hdf5",
    "installing_a_modem_0_Pomaria_0_int_2021-06-08_18-28-21_episode.hdf5",
    "installing_a_printer_0_Beechwood_0_int_2021-05-28_20-02-50_episode.hdf5",
    "installing_a_printer_0_Beechwood_0_int_2021-05-31_15-06-14_episode.hdf5",
    "installing_a_printer_0_Beechwood_0_int_2021-06-02_21-10-06_episode.hdf5",
    "installing_a_printer_0_Beechwood_0_int_2021-06-12_19-15-13_episode.hdf5",
    "installing_a_printer_0_Pomaria_0_int_2021-06-08_18-33-07_episode.hdf5",
    "installing_a_scanner_0_Beechwood_0_int_2021-05-28_20-09-25_episode.hdf5",
    "installing_a_scanner_0_Beechwood_0_int_2021-05-31_15-11-06_episode.hdf5",
    "installing_a_scanner_0_Beechwood_0_int_2021-06-02_21-14-20_episode.hdf5",
    "installing_a_scanner_0_Beechwood_0_int_2021-06-12_19-19-14_episode.hdf5",
    "installing_a_scanner_0_Pomaria_0_int_2021-06-08_18-34-59_episode.hdf5",
    "installing_alarms_0_Merom_1_int_2021-05-23_23-02-24_episode.hdf5",
    "installing_alarms_0_Wainscott_0_int_2021-05-23_22-58-28_episode.hdf5",
    "installing_alarms_0_Wainscott_0_int_2021-06-02_21-19-10_episode.hdf5",
    "installing_alarms_0_Wainscott_0_int_2021-06-04_17-26-03_episode.hdf5",
    "installing_alarms_0_Wainscott_0_int_2021-06-12_19-23-51_episode.hdf5",
    "laying_tile_floors_0_Beechwood_0_int_2021-06-10_19-48-31_episode.hdf5",
    "laying_tile_floors_0_Benevolence_2_int_2021-05-23_18-19-40_episode.hdf5",
    "laying_tile_floors_0_Benevolence_2_int_2021-05-31_15-13-42_episode.hdf5",
    "laying_tile_floors_0_Benevolence_2_int_2021-06-02_21-22-21_episode.hdf5",
    "laying_wood_floors_0_Benevolence_1_int_2021-06-10_19-54-59_episode.hdf5",
    "laying_wood_floors_0_Pomaria_1_int_2021-05-26_16-28-38_episode.hdf5",
    "laying_wood_floors_0_Pomaria_1_int_2021-05-31_15-18-23_episode.hdf5",
    "laying_wood_floors_0_Pomaria_1_int_2021-06-02_21-27-11_episode.hdf5",
    "loading_the_dishwasher_0_Benevolence_1_int_2021-05-27_11-55-49_episode.hdf5",
    "loading_the_dishwasher_0_Benevolence_1_int_2021-05-31_15-23-02_episode.hdf5",
    "loading_the_dishwasher_0_Benevolence_1_int_2021-06-02_21-31-42_episode.hdf5",
    "loading_the_dishwasher_0_Benevolence_1_int_2021-06-19_18-38-19_episode.hdf5",
    "loading_the_dishwasher_0_Wainscott_0_int_2021-06-10_22-31-50_episode.hdf5",
    "locking_every_door_0_Merom_1_int_2021-05-26_16-36-27_episode.hdf5",
    "locking_every_door_0_Merom_1_int_2021-05-31_15-28-08_episode.hdf5",
    "locking_every_door_0_Merom_1_int_2021-06-02_21-37-10_episode.hdf5",
    "locking_every_door_0_Merom_1_int_2021-06-19_18-42-46_episode.hdf5",
    "locking_every_door_0_Pomaria_0_int_2021-06-08_18-38-19_episode.hdf5",
    "locking_every_window_0_Merom_1_int_2021-06-08_18-46-39_episode.hdf5",
    "locking_every_window_0_Wainscott_0_int_2021-05-28_20-15-20_episode.hdf5",
    "locking_every_window_0_Wainscott_0_int_2021-05-31_15-32-21_episode.hdf5",
    "locking_every_window_0_Wainscott_0_int_2021-06-02_22-18-26_episode.hdf5",
    "locking_every_window_0_Wainscott_0_int_2021-06-19_18-47-03_episode.hdf5",
    "making_tea_0_Wainscott_0_int_2021-05-30_11-59-53_episode.hdf5",
    "making_tea_0_Wainscott_0_int_2021-05-31_15-44-16_episode.hdf5",
    "making_tea_0_Wainscott_0_int_2021-06-02_22-31-12_episode.hdf5",
    "making_tea_0_Wainscott_0_int_2021-06-23_18-20-08_episode.hdf5",
    "mopping_floors_0_Benevolence_2_int_2021-05-23_17-49-14_episode.hdf5",
    "mopping_floors_0_Benevolence_2_int_2021-06-03_16-07-23_episode.hdf5",
    "mopping_floors_0_Benevolence_2_int_2021-06-05_19-28-43_episode.hdf5",
    "mopping_floors_0_Ihlen_0_int_2021-05-23_19-45-43_episode.hdf5",
    "moving_boxes_to_storage_0_Ihlen_0_int_2021-06-08_14-59-52_episode.hdf5",
    "moving_boxes_to_storage_0_Merom_0_int_2021-06-08_13-02-25_episode.hdf5",
    "moving_boxes_to_storage_0_Merom_0_int_2021-06-08_13-10-44_episode.hdf5",
    "moving_boxes_to_storage_0_Merom_0_int_2021-06-11_20-04-35_episode.hdf5",
    "moving_boxes_to_storage_0_Merom_0_int_2021-06-13_21-41-42_episode.hdf5",
    "opening_packages_0_Benevolence_2_int_2021-05-23_19-02-06_episode.hdf5",
    "opening_packages_0_Benevolence_2_int_2021-05-31_15-56-21_episode.hdf5",
    "opening_packages_0_Benevolence_2_int_2021-06-03_16-46-42_episode.hdf5",
    "opening_packages_0_Benevolence_2_int_2021-06-23_18-26-11_episode.hdf5",
    "opening_packages_0_Pomaria_2_int_2021-06-08_15-17-28_episode.hdf5",
    "opening_presents_0_Benevolence_2_int_2021-05-24_17-43-18_episode.hdf5",
    "opening_presents_0_Benevolence_2_int_2021-05-31_15-58-51_episode.hdf5",
    "opening_presents_0_Benevolence_2_int_2021-06-03_16-49-46_episode.hdf5",
    "opening_presents_0_Benevolence_2_int_2021-06-23_18-28-08_episode.hdf5",
    "opening_presents_0_Pomaria_2_int_2021-06-08_15-22-15_episode.hdf5",
    "organizing_boxes_in_garage_0_Ihlen_0_int_2021-05-24_21-31-50_episode.hdf5",
    "organizing_boxes_in_garage_0_Ihlen_0_int_2021-05-31_16-01-52_episode.hdf5",
    "organizing_boxes_in_garage_0_Ihlen_0_int_2021-06-05_18-54-10_episode.hdf5",
    "organizing_boxes_in_garage_0_Ihlen_0_int_2021-06-23_18-30-33_episode.hdf5",
    "organizing_file_cabinet_0_Beechwood_0_int_2021-05-30_13-09-40_episode.hdf5",
    "organizing_file_cabinet_0_Beechwood_0_int_2021-06-02_19-12-38_episode.hdf5",
    "organizing_file_cabinet_0_Beechwood_0_int_2021-06-03_19-10-14_episode.hdf5",
    "organizing_file_cabinet_0_Beechwood_0_int_2021-06-23_18-34-40_episode.hdf5",
    "organizing_file_cabinet_0_Pomaria_0_int_2021-06-08_15-27-20_episode.hdf5",
    "organizing_school_stuff_0_Benevolence_2_int_2021-05-24_17-22-00_episode.hdf5",
    "organizing_school_stuff_0_Benevolence_2_int_2021-05-31_16-05-19_episode.hdf5",
    "organizing_school_stuff_0_Benevolence_2_int_2021-06-01_18-49-54_episode.hdf5",
    "packing_adult_s_bags_0_Ihlen_1_int_2021-05-26_16-48-21_episode.hdf5",
    "packing_adult_s_bags_0_Ihlen_1_int_2021-06-03_14-12-35_episode.hdf5",
    "packing_adult_s_bags_0_Ihlen_1_int_2021-06-03_18-35-58_episode.hdf5",
    "packing_adult_s_bags_0_Pomaria_2_int_2021-06-08_15-48-47_episode.hdf5",
    "packing_bags_or_suitcase_0_Merom_1_int_2021-05-28_22-41-34_episode.hdf5",
    "packing_bags_or_suitcase_0_Merom_1_int_2021-06-02_19-20-10_episode.hdf5",
    "packing_bags_or_suitcase_0_Merom_1_int_2021-06-03_18-26-07_episode.hdf5",
    "packing_bags_or_suitcase_0_Pomaria_0_int_2021-06-08_19-04-37_episode.hdf5",
    "packing_boxes_for_household_move_or_trip_0_Beechwood_0_int_2021-05-30_13-23-36_episode.hdf5",
    "packing_boxes_for_household_move_or_trip_0_Beechwood_0_int_2021-06-02_19-37-13_episode.hdf5",
    "packing_boxes_for_household_move_or_trip_0_Beechwood_0_int_2021-06-04_17-31-23_episode.hdf5",
    "packing_boxes_for_household_move_or_trip_0_Ihlen_1_int_2021-06-08_19-16-19_episode.hdf5",
    "packing_car_for_trip_0_Ihlen_0_int_2021-05-24_20-50-17_episode.hdf5",
    "packing_car_for_trip_0_Ihlen_0_int_2021-06-03_14-19-48_episode.hdf5",
    "packing_car_for_trip_0_Ihlen_0_int_2021-06-03_15-42-11_episode.hdf5",
    "packing_car_for_trip_0_Ihlen_0_int_2021-06-23_19-52-28_episode.hdf5",
    "packing_child_s_bag_0_Beechwood_1_int_2021-05-30_13-31-44_episode.hdf5",
    "packing_child_s_bag_0_Beechwood_1_int_2021-06-02_20-01-40_episode.hdf5",
    "packing_child_s_bag_0_Beechwood_1_int_2021-06-03_15-38-25_episode.hdf5",
    "packing_child_s_bag_0_Beechwood_1_int_2021-06-23_19-47-07_episode.hdf5",
    "packing_child_s_bag_0_Wainscott_1_int_2021-06-08_19-21-47_episode.hdf5",
    "packing_food_for_work_0_Beechwood_0_int_2021-05-30_13-38-09_episode.hdf5",
    "packing_food_for_work_0_Beechwood_0_int_2021-06-02_20-13-58_episode.hdf5",
    "packing_food_for_work_0_Beechwood_0_int_2021-06-03_15-33-36_episode.hdf5",
    "packing_food_for_work_0_Beechwood_0_int_2021-06-23_19-42-33_episode.hdf5",
    "packing_food_for_work_0_Ihlen_1_int_2021-06-08_19-36-15_episode.hdf5",
    "packing_lunches_0_Beechwood_0_int_2021-05-30_13-44-21_episode.hdf5",
    "packing_lunches_0_Beechwood_0_int_2021-06-02_20-20-03_episode.hdf5",
    "packing_lunches_0_Beechwood_0_int_2021-06-03_15-27-10_episode.hdf5",
    "packing_lunches_0_Beechwood_0_int_2021-06-23_19-33-21_episode.hdf5",
    "packing_lunches_0_Wainscott_0_int_2021-06-08_19-43-27_episode.hdf5",
    "packing_picnics_0_Pomaria_1_int_2021-06-10_22-15-39_episode.hdf5",
    "packing_picnics_0_Wainscott_0_int_2021-05-23_22-32-44_episode.hdf5",
    "packing_picnics_0_Wainscott_0_int_2021-05-31_16-12-27_episode.hdf5",
    "packing_picnics_0_Wainscott_0_int_2021-06-01_17-18-35_episode.hdf5",
    "packing_picnics_0_Wainscott_0_int_2021-06-23_19-20-51_episode.hdf5",
    "picking_up_take-out_food_0_Beechwood_0_int_2021-05-26_18-00-09_episode.hdf5",
    "picking_up_take-out_food_0_Beechwood_0_int_2021-05-31_16-24-31_episode.hdf5",
    "picking_up_take-out_food_0_Beechwood_0_int_2021-06-01_21-14-32_episode.hdf5",
    "picking_up_take-out_food_0_Beechwood_0_int_2021-06-23_19-12-27_episode.hdf5",
    "picking_up_take-out_food_0_Ihlen_1_int_2021-06-10_22-09-43_episode.hdf5",
    "picking_up_trash_0_Beechwood_0_int_2021-05-26_18-08-11_episode.hdf5",
    "picking_up_trash_0_Beechwood_0_int_2021-05-31_16-32-14_episode.hdf5",
    "picking_up_trash_0_Beechwood_0_int_2021-06-01_17-55-41_episode.hdf5",
    "picking_up_trash_0_Beechwood_0_int_2021-06-23_18-52-05_episode.hdf5",
    "picking_up_trash_0_Merom_1_int_2021-06-08_19-02-09_episode.hdf5",
    "polishing_furniture_0_Ihlen_0_int_2021-05-23_19-54-30_episode.hdf5",
    "polishing_furniture_0_Ihlen_0_int_2021-05-31_16-37-12_episode.hdf5",
    "polishing_furniture_0_Ihlen_0_int_2021-06-01_18-02-31_episode.hdf5",
    "polishing_furniture_0_Ihlen_0_int_2021-06-23_18-55-58_episode.hdf5",
    "polishing_furniture_0_Pomaria_1_int_2021-06-10_21-15-35_episode.hdf5",
    "polishing_shoes_0_Merom_0_int_2021-05-24_17-18-34_episode.hdf5",
    "polishing_shoes_0_Merom_0_int_2021-05-31_16-40-50_episode.hdf5",
    "polishing_shoes_0_Merom_0_int_2021-06-01_21-19-44_episode.hdf5",
    "polishing_shoes_0_Merom_0_int_2021-06-23_18-59-16_episode.hdf5",
    "polishing_shoes_0_Wainscott_0_int_2021-06-10_21-28-31_episode.hdf5",
    "polishing_silver_0_Merom_1_int_2021-05-27_12-02-16_episode.hdf5",
    "polishing_silver_0_Merom_1_int_2021-05-31_17-09-03_episode.hdf5",
    "polishing_silver_0_Merom_1_int_2021-06-03_15-20-26_episode.hdf5",
    "polishing_silver_0_Merom_1_int_2021-06-23_19-02-55_episode.hdf5",
    "polishing_silver_0_Rs_int_2021-06-10_21-22-51_episode.hdf5",
    "preparing_a_shower_for_child_0_Ihlen_0_int_2021-05-23_19-59-05_episode.hdf5",
    "preparing_a_shower_for_child_0_Ihlen_0_int_2021-06-02_20-28-38_episode.hdf5",
    "preparing_a_shower_for_child_0_Ihlen_0_int_2021-06-03_15-16-21_episode.hdf5",
    "preparing_a_shower_for_child_0_Pomaria_2_int_2021-06-10_21-37-08_episode.hdf5",
    "preparing_salad_0_Benevolence_1_int_2021-06-10_19-04-31_episode.hdf5",
    "preparing_salad_0_Pomaria_1_int_2021-05-27_17-09-58_episode.hdf5",
    "preparing_salad_0_Pomaria_1_int_2021-05-31_17-14-46_episode.hdf5",
    "preparing_salad_0_Pomaria_1_int_2021-06-03_15-06-56_episode.hdf5",
    "preparing_salad_0_Pomaria_1_int_2021-06-11_19-43-26_episode.hdf5",
    "preparing_salad_0_Pomaria_1_int_2021-06-22_17-41-47_episode.hdf5",
    "preserving_food_0_Ihlen_1_int_2021-05-28_16-09-56_episode.hdf5",
    "preserving_food_0_Ihlen_1_int_2021-05-31_17-31-57_episode.hdf5",
    "preserving_food_0_Ihlen_1_int_2021-06-07_20-20-39_episode.hdf5",
    "preserving_food_0_Ihlen_1_int_2021-06-22_17-29-42_episode.hdf5",
    "putting_away_Christmas_decorations_0_Merom_1_int_2021-06-10_18-57-09_episode.hdf5",
    "putting_away_Christmas_decorations_0_Wainscott_0_int_2021-06-06_12-31-25_episode.hdf5",
    "putting_away_Christmas_decorations_0_Wainscott_0_int_2021-06-06_16-56-22_episode.hdf5",
    "putting_away_Christmas_decorations_0_Wainscott_0_int_2021-06-06_17-03-25_episode.hdf5",
    "putting_away_Christmas_decorations_0_Wainscott_0_int_2021-06-22_17-17-12_episode.hdf5",
    "putting_away_Halloween_decorations_0_Merom_1_int_2021-06-10_18-49-56_episode.hdf5",
    "putting_away_Halloween_decorations_0_Rs_int_2021-05-25_20-44-19_episode.hdf5",
    "putting_away_Halloween_decorations_0_Rs_int_2021-05-31_17-45-31_episode.hdf5",
    "putting_away_Halloween_decorations_0_Rs_int_2021-06-03_14-47-46_episode.hdf5",
    "putting_away_Halloween_decorations_0_Rs_int_2021-06-22_17-10-45_episode.hdf5",
    "putting_away_toys_0_Benevolence_1_int_2021-06-08_13-37-45_episode.hdf5",
    "putting_away_toys_0_Ihlen_0_int_2021-05-23_20-02-41_episode.hdf5",
    "putting_away_toys_0_Ihlen_0_int_2021-06-02_20-33-37_episode.hdf5",
    "putting_away_toys_0_Ihlen_0_int_2021-06-03_14-43-00_episode.hdf5",
    "putting_away_toys_0_Ihlen_0_int_2021-06-22_17-06-12_episode.hdf5",
    "putting_dishes_away_after_cleaning_0_Beechwood_0_int_2021-06-01_17-47-22_episode.hdf5",
    "putting_dishes_away_after_cleaning_0_Ihlen_1_int_2021-05-23_20-50-21_episode.hdf5",
    "putting_dishes_away_after_cleaning_0_Ihlen_1_int_2021-06-03_14-38-18_episode.hdf5",
    "putting_dishes_away_after_cleaning_0_Ihlen_1_int_2021-06-05_19-01-16_episode.hdf5",
    "putting_dishes_away_after_cleaning_0_Ihlen_1_int_2021-06-22_17-02-22_episode.hdf5",
    "putting_leftovers_away_0_Ihlen_1_int_2021-06-08_13-42-57_episode.hdf5",
    "putting_leftovers_away_0_Pomaria_1_int_2021-05-24_12-53-10_episode.hdf5",
    "putting_leftovers_away_0_Pomaria_1_int_2021-05-31_18-05-14_episode.hdf5",
    "putting_leftovers_away_0_Pomaria_1_int_2021-06-03_14-32-54_episode.hdf5",
    "putting_leftovers_away_0_Pomaria_1_int_2021-06-22_16-56-52_episode.hdf5",
    "putting_up_Christmas_decorations_inside_0_Beechwood_0_int_2021-06-08_13-49-04_episode.hdf5",
    "putting_up_Christmas_decorations_inside_0_Ihlen_1_int_2021-05-28_15-43-40_episode.hdf5",
    "putting_up_Christmas_decorations_inside_0_Ihlen_1_int_2021-06-02_20-49-31_episode.hdf5",
    "putting_up_Christmas_decorations_inside_0_Ihlen_1_int_2021-06-03_14-27-09_episode.hdf5",
    "putting_up_Christmas_decorations_inside_0_Ihlen_1_int_2021-06-22_16-51-08_episode.hdf5",
    "re-shelving_library_books_0_Ihlen_0_int_2021-06-10_21-50-33_episode.hdf5",
    "re-shelving_library_books_0_Rs_int_2021-05-25_20-59-29_episode.hdf5",
    "re-shelving_library_books_0_Rs_int_2021-05-31_18-15-25_episode.hdf5",
    "re-shelving_library_books_0_Rs_int_2021-06-04_13-59-40_episode.hdf5",
    "re-shelving_library_books_0_Rs_int_2021-06-22_16-44-40_episode.hdf5",
    "rearranging_furniture_0_Benevolence_2_int_2021-06-10_21-42-29_episode.hdf5",
    "serving_a_meal_0_Merom_1_int_2021-05-25_21-21-11_episode.hdf5",
    "serving_a_meal_0_Merom_1_int_2021-05-30_22-13-16_episode.hdf5",
    "serving_a_meal_0_Merom_1_int_2021-06-01_18-56-47_episode.hdf5",
    "serving_a_meal_0_Merom_1_int_2021-06-22_16-31-08_episode.hdf5",
    "serving_a_meal_0_Wainscott_0_int_2021-06-08_14-07-06_episode.hdf5",
    "serving_hors_d_oeuvres_0_Merom_1_int_2021-06-08_13-29-03_episode.hdf5",
    "serving_hors_d_oeuvres_0_Wainscott_0_int_2021-05-28_15-23-04_episode.hdf5",
    "serving_hors_d_oeuvres_0_Wainscott_0_int_2021-05-30_22-28-23_episode.hdf5",
    "serving_hors_d_oeuvres_0_Wainscott_0_int_2021-06-01_19-29-25_episode.hdf5",
    "serving_hors_d_oeuvres_0_Wainscott_0_int_2021-06-22_16-15-09_episode.hdf5",
    "setting_mousetraps_0_Beechwood_1_int_2021-05-24_15-31-18_episode.hdf5",
    "setting_mousetraps_0_Beechwood_1_int_2021-05-30_22-39-16_episode.hdf5",
    "setting_mousetraps_0_Beechwood_1_int_2021-06-01_19-40-19_episode.hdf5",
    "setting_mousetraps_0_Beechwood_1_int_2021-06-22_16-00-55_episode.hdf5",
    "setting_mousetraps_0_Benevolence_2_int_2021-06-10_18-40-40_episode.hdf5",
    "setting_up_candles_0_Ihlen_1_int_2021-06-08_17-18-08_episode.hdf5",
    "setting_up_candles_0_Wainscott_0_int_2021-05-30_13-53-09_episode.hdf5",
    "setting_up_candles_0_Wainscott_0_int_2021-06-02_17-55-12_episode.hdf5",
    "setting_up_candles_0_Wainscott_0_int_2021-06-04_14-16-17_episode.hdf5",
    "setting_up_candles_0_Wainscott_0_int_2021-06-19_18-13-42_episode.hdf5",
    "sorting_books_0_Pomaria_1_int_2021-05-30_14-05-08_episode.hdf5",
    "sorting_books_0_Pomaria_1_int_2021-06-02_19-04-53_episode.hdf5",
    "sorting_books_0_Pomaria_1_int_2021-06-04_14-32-22_episode.hdf5",
    "sorting_books_0_Pomaria_1_int_2021-06-19_18-22-02_episode.hdf5",
    "sorting_books_0_Rs_int_2021-06-08_17-30-42_episode.hdf5",
    "sorting_groceries_0_Pomaria_1_int_2021-06-08_17-36-39_episode.hdf5",
    "sorting_groceries_0_Wainscott_0_int_2021-05-23_22-23-02_episode.hdf5",
    "sorting_groceries_0_Wainscott_0_int_2021-06-02_21-08-58_episode.hdf5",
    "sorting_groceries_0_Wainscott_0_int_2021-06-04_14-39-37_episode.hdf5",
    "sorting_groceries_0_Wainscott_0_int_2021-06-22_15-51-47_episode.hdf5",
    "sorting_mail_0_Rs_int_2021-05-26_19-09-39_episode.hdf5",
    "sorting_mail_0_Rs_int_2021-05-30_22-56-33_episode.hdf5",
    "sorting_mail_0_Rs_int_2021-06-04_15-06-41_episode.hdf5",
    "sorting_mail_0_Rs_int_2021-06-19_18-08-23_episode.hdf5",
    "sorting_mail_0_Wainscott_0_int_2021-06-08_17-53-36_episode.hdf5",
    "storing_food_0_Pomaria_1_int_2021-05-22_15-41-40_episode.hdf5",
    "storing_food_0_Pomaria_1_int_2021-05-22_16-51-32_episode.hdf5",
    "storing_food_0_Pomaria_1_int_2021-05-30_23-03-02_episode.hdf5",
    "storing_food_0_Rs_int_2021-05-31_11-45-10_episode.hdf5",
    "storing_food_0_Rs_int_2021-05-31_11-49-30_episode.hdf5",
    "storing_food_0_Rs_int_2021-06-05_19-14-59_episode.hdf5",
    "storing_food_0_Rs_int_2021-06-22_15-44-07_episode.hdf5",
    "storing_the_groceries_0_Beechwood_0_int_2021-05-22_18-39-53_episode.hdf5",
    "storing_the_groceries_0_Wainscott_0_int_2021-05-23_22-13-12_episode.hdf5",
    "storing_the_groceries_0_Wainscott_0_int_2021-06-04_15-16-12_episode.hdf5",
    "storing_the_groceries_0_Wainscott_0_int_2021-06-04_17-13-16_episode.hdf5",
    "storing_the_groceries_0_Wainscott_0_int_2021-06-22_15-37-17_episode.hdf5",
    "thawing_frozen_food_0_Pomaria_1_int_2021-05-23_22-06-10_episode.hdf5",
    "thawing_frozen_food_0_Wainscott_0_int_2021-05-23_22-01-08_episode.hdf5",
    "thawing_frozen_food_0_Wainscott_0_int_2021-06-01_20-55-26_episode.hdf5",
    "thawing_frozen_food_0_Wainscott_0_int_2021-06-05_19-50-38_episode.hdf5",
    "thawing_frozen_food_0_Wainscott_0_int_2021-06-12_19-50-54_episode.hdf5",
    "throwing_away_leftovers_0_Ihlen_1_int_2021-06-04_19-44-50_episode.hdf5",
    "throwing_away_leftovers_0_Ihlen_1_int_2021-06-04_19-48-55_episode.hdf5",
    "throwing_away_leftovers_0_Ihlen_1_int_2021-06-04_19-52-40_episode.hdf5",
    "throwing_away_leftovers_0_Ihlen_1_int_2021-06-05_19-10-02_episode.hdf5",
    "throwing_away_leftovers_0_Ihlen_1_int_2021-06-05_19-57-48_episode.hdf5",
    "throwing_away_leftovers_0_Ihlen_1_int_2021-06-12_19-56-24_episode.hdf5",
    "throwing_away_leftovers_0_Wainscott_0_int_2021-06-08_16-00-28_episode.hdf5",
    "unpacking_suitcase_0_Benevolence_1_int_2021-06-08_17-58-34_episode.hdf5",
    "unpacking_suitcase_0_Ihlen_1_int_2021-05-24_18-12-48_episode.hdf5",
    "unpacking_suitcase_0_Ihlen_1_int_2021-06-02_21-18-54_episode.hdf5",
    "unpacking_suitcase_0_Ihlen_1_int_2021-06-04_15-28-22_episode.hdf5",
    "unpacking_suitcase_0_Ihlen_1_int_2021-06-19_18-01-51_episode.hdf5",
    "vacuuming_floors_0_Benevolence_2_int_2021-05-23_18-27-15_episode.hdf5",
    "vacuuming_floors_0_Benevolence_2_int_2021-06-02_19-31-10_episode.hdf5",
    "vacuuming_floors_0_Benevolence_2_int_2021-06-04_15-35-58_episode.hdf5",
    "vacuuming_floors_0_Benevolence_2_int_2021-06-19_17-56-09_episode.hdf5",
    "vacuuming_floors_0_Ihlen_1_int_2021-06-08_18-03-55_episode.hdf5",
    "washing_cars_or_other_vehicles_0_Ihlen_0_int_2021-05-28_14-03-36_episode.hdf5",
    "washing_cars_or_other_vehicles_0_Ihlen_0_int_2021-06-02_21-25-15_episode.hdf5",
    "washing_cars_or_other_vehicles_0_Ihlen_0_int_2021-06-04_15-43-02_episode.hdf5",
    "washing_cars_or_other_vehicles_0_Ihlen_0_int_2021-06-19_17-53-00_episode.hdf5",
    "washing_dishes_0_Benevolence_1_int_2021-06-08_18-07-48_episode.hdf5",
    "washing_dishes_0_Wainscott_0_int_2021-05-27_16-50-19_episode.hdf5",
    "washing_dishes_0_Wainscott_0_int_2021-05-31_18-28-33_episode.hdf5",
    "washing_dishes_0_Wainscott_0_int_2021-06-04_15-49-38_episode.hdf5",
    "washing_dishes_0_Wainscott_0_int_2021-06-19_17-48-16_episode.hdf5",
    "washing_floor_0_Ihlen_1_int_2021-05-23_21-00-46_episode.hdf5",
    "washing_floor_0_Ihlen_1_int_2021-06-02_21-32-45_episode.hdf5",
    "washing_floor_0_Ihlen_1_int_2021-06-04_15-56-16_episode.hdf5",
    "washing_floor_0_Ihlen_1_int_2021-06-19_17-41-15_episode.hdf5",
    "washing_floor_0_Pomaria_2_int_2021-06-08_18-10-25_episode.hdf5",
    "washing_pots_and_pans_0_Benevolence_1_int_2021-06-07_19-10-24_episode.hdf5",
    "washing_pots_and_pans_0_Benevolence_1_int_2021-06-07_20-01-56_episode.hdf5",
    "washing_pots_and_pans_0_Benevolence_1_int_2021-06-07_20-10-22_episode.hdf5",
    "washing_pots_and_pans_0_Benevolence_1_int_2021-06-22_15-19-31_episode.hdf5",
    "washing_pots_and_pans_0_Pomaria_1_int_2021-06-08_18-15-10_episode.hdf5",
    "watering_houseplants_0_Beechwood_0_int_2021-05-23_21-51-52_episode.hdf5",
    "watering_houseplants_0_Beechwood_0_int_2021-05-31_18-46-34_episode.hdf5",
    "watering_houseplants_0_Beechwood_0_int_2021-06-04_16-03-26_episode.hdf5",
    "watering_houseplants_0_Beechwood_0_int_2021-06-19_17-34-43_episode.hdf5",
    "watering_houseplants_0_Wainscott_0_int_2021-06-08_18-22-28_episode.hdf5",
    "waxing_cars_or_other_vehicles_0_Ihlen_0_int_2021-05-27_16-32-32_episode.hdf5",
    "waxing_cars_or_other_vehicles_0_Ihlen_0_int_2021-06-02_21-49-34_episode.hdf5",
    "waxing_cars_or_other_vehicles_0_Ihlen_0_int_2021-06-03_19-17-09_episode.hdf5",
    "waxing_cars_or_other_vehicles_0_Ihlen_0_int_2021-06-12_19-59-49_episode.hdf5",
]

# TODO: (mjlbach) automate this with google.cloud library once I figure out auth strategy
# def list_demos():
#     """Lists all the blobs in the bucket."""
#     bucket_name = "gibsonchallenge"

#     storage_client = storage.Client()

#     # Note: Client.list_blobs requires at least package version 1.17.0.
#     blobs = storage_client.list_blobs(bucket_name)

#     for blob in blobs:
#         print(blob.name)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template_file = "demo_template.html"
template = templateEnv.get_template(template_file)
outputText = template.render(demo_list = demos)

with open('human_demonstrations.html', 'w') as f:
    f.write(outputText)
