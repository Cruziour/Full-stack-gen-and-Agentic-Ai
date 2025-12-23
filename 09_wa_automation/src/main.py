import pandas as pd
import os
import pyautogui
import time
from datetime import datetime

# Contact list path 
EXCEL_FILE = 'contact.xlsx'
SCHEDULED_TIME = "12:33" 

def send_whatsapp_via_app(phone, name):
    try:
        message = f"Hello {name}, this is whatsapp auto message"

        # Open WhatsApp App 
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('WhatsApp')
        time.sleep(1.5)
        pyautogui.press('enter')

        time.sleep(7) # Thoda extra time loading ke liye

        # Search box focus
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)

        # Number type karna
        pyautogui.write(str(phone))
        time.sleep(4) # Number filter hone ka wait karein
        
        pyautogui.press('enter')
        time.sleep(2)

        # Message bhejna
        pyautogui.write(message)
        time.sleep(1)
        pyautogui.press('enter')

        print(f"✅ Success: Message sent to {name} ({phone})")
        time.sleep(2)
        
        # WhatsApp close karna (Optional: Alt+F4)
        pyautogui.hotkey('alt', 'f4')

    except Exception as e:
        print(f"❌ Error: {name} ({phone}) ko message nahi bhej paye. Wajah: {e}")

def main():
    if not os.path.exists(EXCEL_FILE):
        print(f"Critical Error: {EXCEL_FILE} file nahi mili!")
        return
    
    print(f"Program Started... Scheduled Time: {SCHEDULED_TIME}")

    while True:
        try:
            now = datetime.now().strftime("%H:%M")
            if now == SCHEDULED_TIME:
                print('Time reached! Processing Excel file...')
                
                # Excel read karne mein error handling
                try:
                    df = pd.read_excel(EXCEL_FILE)
                except Exception as e:
                    print(f"Excel read error: {e}")
                    break

                for index, row in df.iterrows():
                    # Check agar data missing hai
                    if pd.isna(row['Number']) or pd.isna(row['Name']):
                        print(f"Skipping row {index}: Name ya Number missing hai.")
                        continue
                        
                    send_whatsapp_via_app(row['Number'], row['Name'])
                    time.sleep(5) # Har message ke beech gap
                
                print('Process Complete.')
                break
            
            time.sleep(30) 

        except KeyboardInterrupt:
            print("\nProgram manualy band kiya gaya.")
            break
        except Exception as e:
            print(f"Loop error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()