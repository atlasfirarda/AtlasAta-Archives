using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms.VisualStyles;

namespace AtlasTemplate__WFA_
{
    internal class Atlas
    {

        public Atlas() { }

        public static bool Select_TabIndex(Control control, Form form)
        {
            var controls = form.Controls.Cast<Control>().Where(c => c.TabStop).OrderBy(c => c.TabIndex).ToList();
            int minIndex = form.Controls.Cast<Control>().Where(c => c.TabStop).OrderBy(c => c.TabIndex).Min(c => c.TabIndex);

            List<int> validIndexes = new List<int>();
            List<int> invalidIndexes = new List<int>();

            foreach (var item in controls)
            {
                if (!validIndexes.Contains(item.TabIndex))
                    validIndexes.Add(item.TabIndex);
                else
                    invalidIndexes.Add(item.TabIndex);
            }

            validIndexes.Clear();

            foreach (var item in invalidIndexes)
                MessageBox.Show($"There is an error here!\n\nInvalid TabIndexes: {item.ToString()}", "Warning!", MessageBoxButtons.OK, MessageBoxIcon.Error);

            invalidIndexes.Clear();

            if (controls.Count == 0)
                return false;

            int currentIndex = controls.FindIndex(c => c == form.ActiveControl);

            if (currentIndex == -1)
                return false;

            if (currentIndex < controls.Count - 1)
            {
                return (form.SelectNextControl(control, true, true, true, false));
            }
            else
            {
                return (controls[minIndex].Focus());
            }
        }

        public static bool Change_Label(Label label, string text = "")
        {
            if(label != null)
            {
                label.Text = text;
                return true;
            } else { return false; }
        }

        public static bool Visibility_Label(Label label)
        {
            if (label != null)
            {

                label.Visible = !label.Visible;

                return true;
            }
            else { return false; }
        }

        public static bool Visibility_Label(Label label, bool Visible = false)
        {
            if(label != null)
            {
                label.Visible = Visible;
                return true;
            }
            else { return false; }
        }

        public static bool Change_TextBox(TextBox textBox, string Text = "")
        {
            if(textBox != null)
            {
                textBox.Text = Text;
                return true;
            }
            else { return false; }
        }

        public static bool Visibility_TextBox(TextBox textBox)
        {
            if(textBox != null)
            {
                textBox.Visible = !textBox.Visible;
                return true;
            } else { return false; }
        }

        public static bool Visibility_TextBox(TextBox textBox, bool Visible = false)
        {
            if (textBox != null)
            {
                textBox.Visible = Visible;
                return true;
            } else { return false; }
        }

        public static bool Change_DarkMode(Control control, Form form)
        {
            if(control != null && form != null)
            {
                var controls = form.Controls.Cast<Control>()
                .OrderBy(c => c.TabIndex)
                .ToList();

                var textboxes = controls.OfType<TextBox>();
                var labels = controls.OfType<Label>();
                var listboxes = controls.OfType<ListBox>();
                var comboboxes = controls.OfType<ComboBox>();
                var buttons = controls.OfType<Button>();
                var radiobuttons = controls.OfType<RadioButton>();
                var checkboxes = controls.OfType<CheckBox>();

                form.BackColor = Color.FromArgb(255, 15, 15, 15);
                form.ForeColor = Color.FromArgb(255, 175, 175, 175);

                if (form.Text.Contains("[Light Mode]"))
                    form.Text = form.Text.Replace(" [Light Mode]", "");
                form.Text = $"{form.Text} [Dark Mode]";

                foreach (var item in textboxes)
                {
                    item.BackColor = Color.FromArgb(255, 35, 35, 35);
                    item.ForeColor = Color.FromArgb(255, 175, 175, 175);

                    item.BorderStyle = BorderStyle.FixedSingle;
                    item.TextAlign = HorizontalAlignment.Center;
                }

                foreach (var item in labels)
                {
                    item.BackColor = Color.Transparent;
                    item.ForeColor = Color.FromArgb(255, 175, 175, 175);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.AutoSize = true;

                    item.BorderStyle = BorderStyle.None;
                }

                foreach (var item in listboxes)
                {
                    item.BackColor = Color.FromArgb(255, 35, 35, 35);
                    item.ForeColor = Color.FromArgb(255, 175, 175, 175);

                    item.BorderStyle = BorderStyle.FixedSingle;
                }

                foreach (var item in comboboxes)
                {
                    item.BackColor = Color.FromArgb(255, 35, 35, 35);
                    item.ForeColor = Color.FromArgb(255, 175, 175, 175);

                    item.FlatStyle = FlatStyle.Flat;
                    item.DropDownStyle = ComboBoxStyle.DropDownList;
                }

                foreach (var item in buttons)
                {
                    item.BackColor = Color.FromArgb(255, 35, 35, 35);
                    item.ForeColor = Color.FromArgb(255, 195, 195, 195);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.AutoSize = true;

                    item.FlatStyle = FlatStyle.Flat;
                    item.FlatAppearance.BorderSize = 1;
                    item.FlatAppearance.BorderColor = Color.FromArgb(255, 75, 75, 75);
                    item.FlatAppearance.MouseDownBackColor = Color.FromArgb(255, 85, 85, 85);
                    item.FlatAppearance.MouseOverBackColor = Color.FromArgb(255, 55, 55, 55);
                }

                foreach(var item in radiobuttons)
                {
                    item.BackColor = Color.Transparent;
                    item.ForeColor = Color.FromArgb(255, 195, 195, 195);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
                }

                foreach (var item in checkboxes)
                {
                    item.BackColor = Color.Transparent;
                    item.ForeColor = Color.FromArgb(255, 195, 195, 195);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;

                    item.FlatStyle = FlatStyle.Standard;
                }

                return true;
            }
            else { return false; }
            
        }

        public static bool Change_LightMode(Control control, Form form)
        {
            if (control != null && form != null)
            {
                var controls = form.Controls.Cast<Control>()
                .OrderBy(c => c.TabIndex)
                .ToList();

                var textboxes = controls.OfType<TextBox>();
                var labels = controls.OfType<Label>();
                var listboxes = controls.OfType<ListBox>();
                var comboboxes = controls.OfType<ComboBox>();
                var buttons = controls.OfType<Button>();
                var radiobuttons = controls.OfType<RadioButton>();
                var checkboxes = controls.OfType<CheckBox>();

                form.BackColor = Color.FromArgb(255, 235, 235, 235);
                form.ForeColor = Color.FromArgb(255, 25, 25, 25);

                if (form.Text.Contains("[Dark Mode]"))
                    form.Text = form.Text.Replace(" [Dark Mode]", "");
                form.Text = $"{form.Text} [Light Mode]";

                foreach (var item in textboxes)
                {
                    item.BackColor = Color.FromArgb(255, 255, 255, 255);
                    item.ForeColor = Color.FromArgb(255, 25, 25, 25);

                    item.BorderStyle = BorderStyle.FixedSingle;
                    item.TextAlign = HorizontalAlignment.Center;
                }

                foreach (var item in labels)
                {
                    item.BackColor = Color.Transparent;
                    item.ForeColor = Color.FromArgb(255, 25, 25, 25);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.AutoSize = true;

                    item.BorderStyle = BorderStyle.None;
                }

                foreach (var item in listboxes)
                {
                    item.BackColor = Color.FromArgb(255, 255, 255, 255);
                    item.ForeColor = Color.FromArgb(255, 25, 25, 25);

                    item.BorderStyle = BorderStyle.FixedSingle;
                }

                foreach (var item in comboboxes)
                {
                    item.BackColor = Color.FromArgb(255, 255, 255, 255);
                    item.ForeColor = Color.FromArgb(255, 25, 25, 25);

                    item.FlatStyle = FlatStyle.Flat;
                    item.DropDownStyle = ComboBoxStyle.DropDownList;
                }

                foreach (var item in buttons)
                {
                    item.BackColor = Color.FromArgb(255, 255, 255, 255);
                    item.ForeColor = Color.FromArgb(255, 25, 25, 25);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.AutoSize = true;

                    item.FlatStyle = FlatStyle.Flat;
                    item.FlatAppearance.BorderSize = 1;
                    item.FlatAppearance.BorderColor = Color.FromArgb(255, 25, 25, 25);
                    item.FlatAppearance.MouseDownBackColor = Color.FromArgb(195, 195, 195, 195);
                    item.FlatAppearance.MouseOverBackColor = Color.FromArgb(235, 235, 235, 235);
                }

                foreach (var item in radiobuttons)
                {
                    item.BackColor = Color.Transparent;
                    item.ForeColor = Color.FromArgb(255, 25, 25, 25);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
                }

                foreach (var item in checkboxes)
                {
                    item.BackColor = Color.Transparent;
                    item.ForeColor = Color.FromArgb(255, 25, 25, 25);

                    item.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                    item.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;

                    item.FlatStyle = FlatStyle.Standard;
                }

                return true;
            }
            else { return false; }
        }

        public static bool change_Mode(Control control, Form form, bool mode = false)
        {
            if(control != null && form != null)
            {
                if (mode)
                {
                    Change_LightMode(control, form);
                }
                else
                {
                    Change_DarkMode(control, form);
                }

                return true;
            }
            else { return false; }
        }

        public static Task wait(int miliseconds, int seconds)
        {
            if(miliseconds != 0)
            {
                return Task.Delay(miliseconds);
            } else if(seconds != 0)
            {
                return Task.Delay((int)seconds); ;
            }
            else { return Task.Delay(0); }
        }

    }
}
