from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty #allows to set obj properties to design file properties
from kivy.lang import Builder # allows for defining of custom design files
from kivy.core.window import Window # allows for defining of app color theme

# Designate Our kv.design file
Builder.load_file('design_cal.kv') # or ...load_string
Window.size = (400,600)

class MyLayout(Widget):
    def backspace(self):
        prior = self.ids.calc_input.text 
        if len(list(prior)) == 1:
            prior = '0'
        else:
            prior = prior[:-1]
        self.ids.calc_input.text = prior
    def button_press(self,button):
        #create a variable to hold prior text values
        prior = self.ids.calc_input.text

        #determine if 0 is sitting in there
        try:

            if len(prior) > 2:

                val1 = prior[-1]
                val2 = prior[-2]

                if '*' in val1  and '/' in val2 or '*' in val2 and '/' in val1: 
                    self.ids.calc_input.text = 'Error'
        except:
            pass

        if prior == 'Error':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text ='{button}'.format(button=button)

        elif prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = '{button}'.format(button=button)


        else:
            self.ids.calc_input.text = '{prior}{button}'.format(prior=prior,button=button)
        

    def clear_all(self):
        self.ids.calc_input.text = '0'

    def math_sign(self,sign):
        #Create a variable that holds all the values in prior textinput box
        prior_value = self.ids.calc_input.text

        # Add a modulus sign at the end 
        self.ids.calc_input.text ='{previous_val}{sign}'.format(previous_val = prior_value,sign = sign) 

    def dot(self,value):
        prior = self.ids.calc_input.text
        
        # not yet inmplemented the dot sign when there's a math sign is parsed
        # Split our text box by +
        num_list = prior.split('+')
        
        if "+" in prior and value not in num_list[-1]:
            # Add a decimal to the end

            prior = "{prior}{value}".format(prior=prior,value=value)
            # Output back to the text box
            self.ids.calc_input.text = prior


        elif value in prior:
            pass
        else:

            prior = "{prior}{value}".format(prior=prior,value=value)

            self.ids.calc_input.text = prior

    # Create a function to make text box negative and positive
    def pos_neg(self):
        #get prior content from text input box
        prior = self.ids.calc_input.text
        # Text to see if there's a - sign 
        if '-' in prior:
            self.ids.calc_input.text = '{prior}'.format(prior = prior.replace('-',''))
        else:
            self.ids.calc_input.text = '-{prior}'.format(prior=prior)

    def equals(self):
        prior = self.ids.calc_input.text
        
        # Error handling for divide by zero

        try:
            # Evaluate Math operations
            # todo: Employ eval security measures
            answer = eval(prior)

            # Output the answer on-screen
            self.ids.calc_input.text = str(answer)
        except ZeroDivisionError:
            self.ids.calc_input.text = "Error"

'''
        #addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0

            #loop through our list
            for number in num_list:
                answer = answer + float(number)
            self.ids.calc_input.text = str(answer)
'''

class Awesome(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Awesome().run()
