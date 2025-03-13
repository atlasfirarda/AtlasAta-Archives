using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics.Eventing.Reader;
using System.Drawing;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AtlasTemplate__WFA_
{
    public partial class Template : Form
    {
        public Template()
        {
            InitializeComponent();
        }

        public static Form form = Template.ActiveForm;

        private Control control;

        private bool changeMode = false;

        private async void Load_Template(object sender, EventArgs e)
        {
            await Atlas.wait(miliseconds:24, seconds:0);

            if (form.ActiveControl is Control control)
            {
                Atlas.change_Mode(control, form, changeMode);

                changeMode = !changeMode;
            }
        }

        private void KeyDown_Template(object sender, KeyEventArgs key)
        {
            if(key.KeyCode.Equals(Keys.Escape))
            {
                Application.Exit();
            }
            else if(key.KeyCode.Equals(Keys.Enter))
            {
                if(form.ActiveControl is Control control)
                {
                    Atlas.Select_TabIndex(control, form);
                    key.SuppressKeyPress = true;
                }
            }
            else if(key.KeyCode.Equals(Keys.NumPad0))
            {
                if (form.ActiveControl is Control control)
                {
                    Atlas.change_Mode(control, form, changeMode);
                    key.SuppressKeyPress = true;

                    changeMode = !changeMode;
                }
            }
        }
    }
}
