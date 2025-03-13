namespace AtlasTemplate__WFA_
{
    partial class Template
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            textBox4 = new TextBox();
            textBox5 = new TextBox();
            textBox6 = new TextBox();
            label1 = new Label();
            listBox1 = new ListBox();
            button1 = new Button();
            comboBox1 = new ComboBox();
            radioButton1 = new RadioButton();
            checkBox1 = new CheckBox();
            SuspendLayout();
            // 
            // textBox1
            // 
            textBox1.BorderStyle = BorderStyle.FixedSingle;
            textBox1.Location = new Point(363, 178);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(100, 25);
            textBox1.TabIndex = 0;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(363, 209);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(100, 25);
            textBox2.TabIndex = 1;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(363, 240);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(100, 25);
            textBox3.TabIndex = 2;
            // 
            // textBox4
            // 
            textBox4.Location = new Point(363, 271);
            textBox4.Name = "textBox4";
            textBox4.Size = new Size(100, 25);
            textBox4.TabIndex = 3;
            // 
            // textBox5
            // 
            textBox5.Location = new Point(363, 302);
            textBox5.Name = "textBox5";
            textBox5.Size = new Size(100, 25);
            textBox5.TabIndex = 4;
            // 
            // textBox6
            // 
            textBox6.Location = new Point(363, 333);
            textBox6.Name = "textBox6";
            textBox6.Size = new Size(100, 25);
            textBox6.TabIndex = 5;
            textBox6.TabStop = false;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.BackColor = Color.Transparent;
            label1.Location = new Point(384, 157);
            label1.Name = "label1";
            label1.Size = new Size(56, 18);
            label1.TabIndex = 6;
            label1.Text = "label1";
            // 
            // listBox1
            // 
            listBox1.FormattingEnabled = true;
            listBox1.Items.AddRange(new object[] { "Atlas", "Selam", "Selami" });
            listBox1.Location = new Point(31, 178);
            listBox1.Name = "listBox1";
            listBox1.Size = new Size(283, 174);
            listBox1.TabIndex = 7;
            // 
            // button1
            // 
            button1.Location = new Point(213, 399);
            button1.Name = "button1";
            button1.Size = new Size(161, 45);
            button1.TabIndex = 8;
            button1.Text = "button1";
            button1.UseVisualStyleBackColor = true;
            // 
            // comboBox1
            // 
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox1.FlatStyle = FlatStyle.Flat;
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "Selam", "Atlas", "Kela" });
            comboBox1.Location = new Point(509, 358);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(170, 25);
            comboBox1.TabIndex = 9;
            // 
            // radioButton1
            // 
            radioButton1.AutoSize = true;
            radioButton1.Location = new Point(557, 144);
            radioButton1.Name = "radioButton1";
            radioButton1.Size = new Size(122, 22);
            radioButton1.TabIndex = 10;
            radioButton1.TabStop = true;
            radioButton1.Text = "radioButton1";
            radioButton1.UseVisualStyleBackColor = true;
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(557, 172);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(99, 22);
            checkBox1.TabIndex = 11;
            checkBox1.Text = "checkBox1";
            checkBox1.UseVisualStyleBackColor = true;
            // 
            // Template
            // 
            AutoScaleMode = AutoScaleMode.None;
            BackColor = Color.FromArgb(235, 235, 235);
            BackgroundImageLayout = ImageLayout.Center;
            ClientSize = new Size(904, 581);
            Controls.Add(checkBox1);
            Controls.Add(radioButton1);
            Controls.Add(comboBox1);
            Controls.Add(button1);
            Controls.Add(listBox1);
            Controls.Add(label1);
            Controls.Add(textBox6);
            Controls.Add(textBox5);
            Controls.Add(textBox4);
            Controls.Add(textBox3);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            DoubleBuffered = true;
            Font = new Font("JetBrains Mono", 10F);
            ForeColor = Color.FromArgb(15, 15, 15);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            KeyPreview = true;
            Margin = new Padding(3, 4, 3, 4);
            Name = "Template";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Atlas Template";
            Load += Load_Template;
            KeyDown += KeyDown_Template;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBox1;
        private TextBox textBox2;
        private TextBox textBox3;
        private TextBox textBox4;
        private TextBox textBox5;
        private TextBox textBox6;
        private Label label1;
        private ListBox listBox1;
        private Button button1;
        private ComboBox comboBox1;
        private RadioButton radioButton1;
        private CheckBox checkBox1;
    }
}