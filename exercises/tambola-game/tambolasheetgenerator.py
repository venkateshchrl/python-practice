import random
import numpy as np

class SheetGenerator():    
    def __init__(self):
        self.master_number_list = []
        self.tickets = []
    
    def __generate_master_list(self):
        self.master_number_list = []
        for index in range(1, 91, 10):
            temp_number_list = list(range(index, index+10))
            random.shuffle(temp_number_list)
            self.master_number_list.append(temp_number_list)

    def generateSheet(self):
        self.tickets = []
        self.__generate_master_list()
        while len(self.tickets) < 6:
            ticket = []
            while len(ticket) < 3:
                ticket_row = [0]*9
                count = 0
                i = 0
                skip_len_logic = False
                while count < 5:
                    iterator_number_list = list(range(0, 9))
                    random.shuffle(iterator_number_list)
                    while iterator_number_list:
                        if(count > 4):
                            break
                        index = 0
                        if(len(self.tickets) == 4 or len(self.tickets) == 5):
                            is_master_number_list_syncronized = False
                            while i < len(self.master_number_list):
                                if ((len(self.tickets) == 4 and len(self.master_number_list[i]) > 2) or (len(self.tickets) == 5 and len(self.master_number_list[i]) > 1)):
                                    is_master_number_list_syncronized = False
                                    index = i
                                    if(ticket_row[index] != 0):
                                        is_master_number_list_syncronized = True
                                    i += 1
                                    break
                                is_master_number_list_syncronized = True
                                i += 1
                            if(is_master_number_list_syncronized == True):
                                index = iterator_number_list.pop(0)
                            if(len(self.master_number_list[index]) > 0):
                                if(ticket_row[index] == 0):
                                    ticket_row[index] = self.master_number_list[index].pop()
                                    count += 1
                            if count < 5 and (i-1 == (len(self.master_number_list)-1)):
                                i = 0
                                break
                        else:    
                            index = iterator_number_list.pop(0)
                            if(len(self.master_number_list[index]) > 0 and (len(self.master_number_list[index]) > (10-(len(self.tickets)+2)) or skip_len_logic)):
                                if(len(ticket) == 2 and (ticket[0][index] != 0 and ticket[1][index] != 0)):
                                    continue
                                # if(len(tickets) > 2):
                                #     repeated_count = 0
                                #     for i in range(len(tickets[len(tickets)-1])):
                                #         if(tickets[len(tickets)-1][i][index] != 0):
                                #             repeated_count += 1
                                #     if(len(ticket) > 0 and repeated_count > 1):
                                #         if(len(ticket) < 2):
                                #             if(ticket[len(ticket) - 2][index] != 0):
                                #                 continue
                                #         elif(ticket[len(ticket) - 1][index] != 0 or ticket[len(ticket) - 2][index] != 0):
                                #             continue
                                #     if(ticket_row[index] == 0):
                                #         ticket_row[index] = master_number_list[index].pop()
                                #         count += 1
                                # else:
                                if(ticket_row[index] == 0):
                                    ticket_row[index] = self.master_number_list[index].pop()
                                    count += 1
                                # if(len(master_number_list[index]) == 0):
                                #     del master_iterator_list[master_iterator_list.index(index)]
                            #else:
                                #iterator_number_list.append(index)
                            # i += 1
                            # if count < 5 and i-1 == (len(master_number_list)-1):
                            #     i = 0
                            #     skip_len_logic = True
                            if(len(iterator_number_list) == 0 and count < 5):
                                skip_len_logic = True

                ticket.append(ticket_row)
            self.tickets.append(ticket)
        self.__validate_all_numbers()
        return self.__formatSheet()
    
    def __formatSheet(self):
        self_str = "="*44 + "\n"
        for i in range(len(self.tickets)):
            self_str += "-"*44 + "\n"
            self_str += "-"*18 + "TICKET-"+str((i+1))+"-"*18 +"\n"
            self_str += "-"*44 + "\n"
            for j in range(len(self.tickets[i])):
                for k in range(len(self.tickets[i][j])):
                    value = str(self.tickets[i][j][k]) if self.tickets[i][j][k] >= 10 else " " + str(self.tickets[i][j][k])
                    self_str += value + " | "
                    if(k == len(self.tickets[i][j])-1):
                        self_str += "\n"
            self_str += "-"*44 + "\n"
        self_str += "="*44 + "\n"
        return self_str

    def __validate_all_numbers(self):
        self_array = np.array(self.tickets)
        validate_counter = 0
        for i in range(0, 91)[1:]:
            result = np.where(self_array == i)
            if(result[0].size > 0):
                validate_counter += 1
        
        if(validate_counter == 90):
            print("All numbers available")
