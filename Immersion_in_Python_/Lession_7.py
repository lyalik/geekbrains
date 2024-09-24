# # # # from file_utils import batch_rename_files
# # # #
# # # # # Пример использования функции
# # # # directory = "lession_7"
# # # # desired_name = "newname"
# # # # num_digits = 3
# # # # src_extension = ".txt"
# # # # dest_extension = ".md"
# # # # name_range = (3, 6)
# # # #
# # # # batch_rename_files(directory, desired_name, num_digits, src_extension, dest_extension, name_range)
# # #
# # # #2
# # #
# # # from archive_utils import create_zip_archive
# # #
# # # # Пример использования функции
# # # source_directory = "lession_7"
# # # target_zip_file = "lession_7.zip"
# # #
# # # create_zip_archive(source_directory, target_zip_file)
# #
# # #3
# #
# # from cleanup_utils import delete_old_files
# #
# # # Пример использования функции
# # directory_to_clean = "path/to/your/directory"
# # days_threshold = 30 # Удалять файлы, которые не изменялись более 30 дней
# #
# # delete_old_files(directory_to_clean, days_threshold)
#
# #4
# from search_utils import find_files_by_extension
#
# # Пример использования функции
# directory_to_search = "lession_7"
# file_extension = ".md"
#
# found_files = find_files_by_extension(directory_to_search, file_extension)
#
# print(f"Найдено {len(found_files)} файлов с расширением {file_extension}.")