def solution(cards):
	def swap(a_idx):
		print(f"In swap {cards[cur_idx]=}")
		tmp = cards[cur_idx][a_idx]
		cards[cur_idx][a_idx] = cards[next_idx][a_idx]
		cards[next_idx][a_idx] = tmp
		print(f"In swap {cards[cur_idx]=}")
	total_sum = 0
	card_len = len(cards)
	visisted = [False for _ in range(card_len)]
	for cur_idx, cur_card in enumerate(cards):
		if visisted[cur_idx] == True:
			continue
		visisted[cur_idx] = True
		min_c_idx = cur_card.index(min(cur_card))

		for next_idx in range(cur_idx + 1, card_len):
			if visisted[next_idx] == True:
				continue
			next_card = cards[next_idx]
			min_n_idx = next_card.index(min(next_card))
			if min_n_idx == min_c_idx:
				continue
			if cur_card[min_c_idx] < next_card[min_c_idx] and \
				cur_card[min_n_idx] > next_card[min_n_idx]:				
				print(f"before {cards[cur_idx]=}")
				print(f"before {cards[next_idx]=}")
				swap(min_c_idx)
				swap(min_n_idx)
				total_sum += min(cards[cur_idx])
				total_sum += min(cards[next_idx])
				print(f"after {cards[cur_idx]=}")
				print(f"after {cards[next_idx]=}")
				visisted[next_idx] = True
				break
		else:
			total_sum += min(cur_card)
	return total_sum


cards = [[10, 5, 15], [5, 15, 10], [10, 11, 9]]
print(solution(cards))
