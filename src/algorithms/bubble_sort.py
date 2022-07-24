import draw_information

def bubble_sort(draw_info: draw_information.DrawInformation, ascending=True):
	lst = draw_info.lst

	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_info.draw_list({j: draw_info.GREEN, j + 1: draw_info.RED}, True)
				yield True
	
	return lst