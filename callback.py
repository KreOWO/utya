from exec_cmd import exec_cmd
from asyncs import say
from opts import opts


def callback(voice, varable):
    if not varable.name_said:
        if voice in ['у тебя', 'утёнок', 'утя', 'утенок']:
            say('Слушаю вас')
            varable.name_said = True
    else:
        if varable.long_text:
            if voice in ['конец текста', 'перестань печатать']:
                varable.last_text = []
                say('Закончил')
                varable.long_text = False
            elif voice in ['отмена', 'вернуть', 'назад'] and varable.last_text != []:
                exec_cmd('kb_write', '', len(varable.last_text[-1]) * '\b', varable)
                varable.last_text = varable.last_text[:-1]
            else:
                varable.last_text.append(voice + ' ')
                exec_cmd('kb_write', '', voice + ' ', varable)
        else:
            cmd = voice
            chcmd = cmd
            new_cmd = []
            for i, j in opts.items():
                for g in j:
                    if g != '' and g in chcmd:
                        new_cmd.append([i, g])
                        chcmd = chcmd.replace(g, '')
                        break
            
            if len(new_cmd) > 0:
                
                new_pos_cmds = []
                for i in range(len(new_cmd)):
                    new_pos_cmds.append([cmd.index(new_cmd[i][1]), new_cmd[i]])
                
                new_pos_cmds.sort()
                new_cmd = [j for i, j in new_pos_cmds]
                
                cmd = cmd.split(new_cmd[0][1])[1]
                for i in range(len(new_cmd) - 1):
                    cmd = cmd.split(new_cmd[i + 1][1])
                    new_cmd[i].append(cmd[0])
                    cmd = cmd[1]
                new_cmd[-1].append(cmd)
                
                varable.last_task = new_cmd
                print(varable.last_task)
                
                for i in range(len(new_cmd)):
                    exec_cmd(*new_cmd[i], varable)
    
    return varable
