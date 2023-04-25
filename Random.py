# --  Bring in the .NET stuff, and reference Forms and drawing
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

#   get the objects you need from forms and drawing
from System.Windows.Forms import Form, Label, Button, TextBox
from System.Drawing import Point, ContentAlignment

#-- The way python works with events, you have to make a class out of your form.  
#   Then the objects 
#    you add are available in event functions.
class TowerForm(Form):
	def __init__(self):
#-- First, make the form (self)
		self.text="Tower Simulation Tool"
		self.Height=500
		self.Width=250

#-- Create a Simple Text Label describing the tool
#   it is not self.label because we are not going to access it in event functions
		lbl1 = Label()
		lbl1.Text = "This is the Tower of Test Tool. \n\
			Please Enter values and click OK to run the \
			model and get new results\n"
		lbl1.Height = 50 
		lbl1.Width = 200

#-- Create the Text Labels and text boxes to get Dimensions and Pressure
#   We need to get to the textboxes so we will make them part of the class
#
#   some constants to make the positioning easier
		x1 = 10
		y1 = 80
		w1 = 70
		w2 = 80
		x2 = x1 + w1 + 10
#   Make the labels for the text boxes.  This is done in the Labe() call with 
#   Name = Value arguments 
#   instead of object.name = value to save space.  All in one line instead of 
#   four lines.
#     The alighment is done so that the labels are all right justified to line 
#     up with the boxes. Set ContentAlignment.MiddleRight to mr to save space
		mr = ContentAlignment.MiddleRight
		lb_Length=Label(Text="Length", Width=w1,TextAlign=mr)
		lb_Width  = Label(Text="Width",   Width = w1, TextAlign=mr)
		lb_Height = Label(Text="Height",  Width = w1, TextAlign=mr)
		lb_Press  = Label(Text="Pressure",Width = w1, TextAlign=mr)

#   Make the text boxes. Note that these are put in the self. class. 
#   We do this so that when the OK 
#   button is pushed, we have access to the text boxes and therefore the values 
#   typed within

		self.tb_Length = TextBox(Width = w2)
		self.tb_Width  = TextBox(Width = w2)
		self.tb_Height = TextBox(Width = w2)
		self.tb_Press  = TextBox(Width = w2)

#   Specify the location for the label and the text boxes.  Move down by 
#   30 after each line
		lb_Length.Location = Point(x1,y1)
		self.tb_Length.Location = Point(x2,y1)
		y1 = y1 + 30
		lb_Width.Location = Point(x1,y1)
		self.tb_Width.Location = Point(x2,y1)
		y1 = y1 + 30
		lb_Height.Location = Point(x1,y1)
		self.tb_Height.Location = Point(x2,y1)
		y1 = y1 + 30
		lb_Press.Location = Point(x1,y1)
		self.tb_Press.Location = Point(x2,y1)

#   Make an OK and a Cancel Button
		okBut = Button(Text="OK", Width=50)
		okBut.Location = Point(30,430)
#       This is where you specify the funtion to be called when the button is clicked
#       note that you call the function self.functionname.
		okBut.Click += self.okButPressed 

		cancelBut = Button(Text="Cancel", Width=50)
		cancelBut.Location = Point(110,430)
		cancelBut.Click += self.cancelButPressed

#   Put everything on the form (some sort of list and loop would make this easier)
		self.Controls.Add(lbl1)
		self.Controls.Add(lb_Length)
		self.Controls.Add(self.tb_Length)
		self.Controls.Add(lb_Width)
		self.Controls.Add(self.tb_Width)
		self.Controls.Add(lb_Height)
		self.Controls.Add(self.tb_Height)
		self.Controls.Add(lb_Press)
		self.Controls.Add(self.tb_Press)
		self.Controls.Add(okBut)
		self.Controls.Add(cancelBut)

#-- Now define the button event functions as part of the class
#
# Cancel simply closes the form down.  Nothing fancy
	def cancelButPressed(self, sender, args ):
		print 'Closing the Window... Bye...\n'
		self.Close()

# OK prints the values of the text boxes to the console
#   This will be replaced with calls to workbench for the next step
	def okButPressed(self, sender, args ):
		print 'Values Entered:\n'
		print '  Length: %s\n' %self.tb_Length.Text
		print '   Width: %s\n' %self.tb_Width.Text
		print '  Height: %s\n' %self.tb_Height.Text
		print 'Pressure: %s\n' %self.tb_Press.Text
		self.Close()
#---------End of class definition


# Instantiate the form and make the form visible
print '=======================================\n'
print 'Opening the Windows...\n'
myForm = TowerForm()
Form.ShowDialog(myForm)
